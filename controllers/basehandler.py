# -*- coding: utf-8 -*-

import sys

sys.path.append('../conf')
from conf import REDISIP
from conf import REDISPORT
from conf import REDISDB
from conf import REDISPSW

sys.path.append("../database")
#from database import redisBus

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    def initialize(self):
        self.set_header('Server', 'JJ-ADjust-CallBack-Server')
        #self.rdb = redisBus(REDISIP, REDISPORT, REDISDB, REDISPSW)
        
