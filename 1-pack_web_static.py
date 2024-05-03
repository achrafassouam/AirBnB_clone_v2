#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder
"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"
    result = local("tar -czvf {} web_static".format(archive_name))
    if result.succeeded:
        return archive_name
    else:
        return None

# Example usage:
if __name__ == "__main__":
    archive_path = do_pack()
    if archive_path:
        print(f"Archive created: {archive_path}")
    else:
        print("Archive creation failed.")
