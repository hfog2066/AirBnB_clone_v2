#!/usr/bin/python3
""" Does deployment"""

from fabric.api import *
import os
from datetime import datetime
import tarfile

env.hosts = ["35.237.254.224", "34.73.109.66"]
env.user = "ubuntu"


def deploy():
    """ Calls all tasks to deploy archive to webservers"""
    tar = do_pack()
    if not tar:
        return False
    return do_deploy(tar)


def do_pack():
    """ Creates tar archive"""
    savedir = "versions/"
    filename = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    if not os.path.exists(savedir):
        os.mkdir(savedir)
    with tarfile.open(savedir + filename, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(savedir + filename):
        return savedir + filename
    else:
        return None
