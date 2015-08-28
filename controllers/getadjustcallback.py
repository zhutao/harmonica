# -*- coding: utf-8 -*-

from tornado.gen import coroutine

from basehandler import BaseHandler


class GetADjustCallBackInstall(BaseHandler):
    @coroutine
    def get(self):
        self.finish()


class GetADjustCallBackClick(BaseHandler):
    @coroutine
    def get(self):
        self.finish()


class GetADjustCallBackSession(BaseHandler):
    @coroutine
    def get(self):
        self.finish()        
