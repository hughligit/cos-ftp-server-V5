# -*- coding:utf-8 -*-

from pyftpdlib.handlers import FTPHandler


class CosFtpHandler(FTPHandler):
    def __init__(self, *args, **kwargs):
        FTPHandler.__init__(self, *args, **kwargs)

    def ftp_MLST(self, path):
        return self.ftp_LIST(path)
