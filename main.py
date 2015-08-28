# -*- coding: utf-8 -*-

import sys
sys.path.append("../conf")
import conf

from tornado.options import parse_command_line, options, define
from tornado.netutil import bind_sockets
from tornado.process import fork_processes
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from controllers import router

define('port', default = 4587, help = 'run on the given port', type = int)
define('debug', default = False, help = 'run on the debug status', type = bool)

def main():
    parse_command_line()
    
    settings = {
        'debug': options.debug
    }

    sockets = bind_sockets(options.port)
    fork_processes(0)
    application = router(settings)
    _http_server = HTTPServer(application)
    _http_server.add_sockets(sockets)
    IOLoop.current().start()


if __name__ == '__main__':
    main()
