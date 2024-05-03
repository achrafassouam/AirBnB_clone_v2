#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generate a tar gzipped archive
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"
    result = local("tar -czvf {} web_static".format(archive_name))
    if result.succeeded:
        return archive_name
    else:
        return None
