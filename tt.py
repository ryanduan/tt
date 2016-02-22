# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'TT'

__release__ = 'RELEASE'

import os
import tornado.options
from tornado.options import options, define
import tornado.web
from tornado.httpserver import HTTPServer
import tornado.ioloop
from sqlalchemy.orm import scoped_session, sessionmaker
import logging as log
from models.dao import Dao
from models.config import Config

from controller.index import Index


class Application(tornado.web.Application):
    """"""
    def __init__(self):
        urls = [
            (Index.url, Index),
        ]

        settings = dict(
            xsrf_cookies=False,
            debug=False,
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
        )

        # self.db_session = scoped_session(sessionmaker(bind=Dao.engine()))
        tornado.web.Application.__init__(self, urls, **settings)


if __name__ == '__main__':
    """"""
    options.define(name='config', default='TT')
    options.define(name='port', default=8002)
    options.define(name='process', default=1)
    options.define(name='server', default='total')

    tornado.options.parse_command_line()
    config = Config(options.config)
    Dao.init_db_uri(options.config)
    # for dev and test
    # if options.config != __release__:
    #     Dao.init_schema()

    app = Application()

    app.config = options.config

    app.rds = Dao.rds()

    log.info('Starting {} server... Listening port: {}'.format(options.server, options.port))
    try:
        server = HTTPServer(app, xheaders=True)
        server.bind(int(options.port))
        server.start(num_processes=int(options.process))
        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        log.error('{} can not running:\n{}'.format(options.server, e), exc_info=True)
        tornado.ioloop.IOLoop.instance().stop()
