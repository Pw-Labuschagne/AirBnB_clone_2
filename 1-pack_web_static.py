#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Function to compress directory before sending
    Return: path to archive on success;
    Return: on fail None
    """

    current_time = datetime.now()
    current_time = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + current_time + '.tgz'

    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    if result.succeeded:
        return archive_path
    return None
