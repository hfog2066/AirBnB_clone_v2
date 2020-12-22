#!/usr/bin/python3
"Generates a .tgz"

import tarfile
import os
from datetime import datetime


def do_pack():
    """ Create tar """
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
