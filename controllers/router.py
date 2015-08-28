# -*- coding: utf-8 -*-

from tornado.web import Application

from getadjustcallback import GetADjustCallBackInstall
from getadjustcallback import GetADjustCallBackClick
from getadjustcallback import GetADjustCallBackSession

def router(settings):
    return Application([
        (r"/getadjustcallback/install/", GetADjustCallBackInstall),
        (r"/getadjustcallback/click/", GetADjustCallBackClick),
        (r"/getadjustcallback/session/", GetADjustCallBackSession),
    ], **settings)
