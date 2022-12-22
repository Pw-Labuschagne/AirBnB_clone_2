#!/usr/bin/python3
"""Compress web static package
"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Function to compress directory before sending
    Return: path to archive on success;
    Return: on fail
    """

    dateNow = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dateNow.year,
                                                         dateNow.month,
                                                         dateNow.day,
                                                         dateNow.hour,
                                                         dateNow.minute,
                                                         date_now.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file

