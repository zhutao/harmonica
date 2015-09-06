# -*- coding: utf-8 -*-

from tornado.gen import coroutine

from basehandler import BaseHandler


class RestAPI(BaseHandler):
    @coroutine
    def get(self):
        self.write('Hello Tornado.')
        self.finish()


    @coroutine
    def post(self):
        self.finish()


    @coroutine
    def put(self):
        self.finish()


    @coroutine
    def delete(self):
        self.finish()

    @coroutine
    def option(self):
        self.finish()