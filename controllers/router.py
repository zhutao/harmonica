# -*- coding: utf-8 -*-

from tornado.web import Application

from restapi import RestAPI

def router(settings):
    return Application([
        (r"/restapi", RestAPI),
    ], **settings)
