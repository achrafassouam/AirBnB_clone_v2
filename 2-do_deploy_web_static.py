#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers using the function do_deploy
"""

from fabric.api import env, put, run, local
import os

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual IP addresses

def do_deploy(archive_path):
    """
    Distributes an archive to web servers using the function do_deploy
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract the archive to the folder /data/web_static/releases/<archive filename without extension>
        archive_filename = os.path.basename(archive_path)
        release_folder = '/data/web_static/releases/' + archive_filename[:-4]
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current linked to the new version
        run('ln -s {} /data/web_static/current'.format(release_folder))

        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    archive_path = do_pack()  # Assuming do_pack() returns the archive path
    if archive_path:
        result = do_deploy(archive_path)
        if result:
            print("Deployment successful!")
        else:
            print("Deployment failed.")
    else:
        print("Archive creation failed.")

