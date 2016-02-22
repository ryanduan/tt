# -*- coding: utf-8 -*-

"""
集成RequestHandler类，主要是完成数据库连接以及一些大部分controller公用的方法属性等。
计划加入property,这样一些方法就可以当做属性来调用了。
"""

__author__ = 'TT'

import traceback
import sys
import json
import itertools
import base64
import math
import time
import hashlib

from tornado.web import RequestHandler
from sqlalchemy.exc import SQLAlchemyError

import logging as log
from models.dao import Dao
from models.config import Config
from models.util import cached_property


class BaseController(RequestHandler):
    """"""
    # 用与do_write 设置的header
    content_type = None

    def initialize(self):
        """"""
        # self.db_session = self.application.db_session
        self.rds = self.application.rds

    def prepare(self):
        """"""

    def on_finish(self):
        """"""
        # self.db_session.remove()
        # self.exc_info = None

    # def commit(self):
    #     """:returns bool
    #     session的commit操作，如果操作完成，返回True，失败返回False。
    #     失败的时候，会rollback()，记录log，http返回数据库错误什么的，随意就好了。
    #     """
    #     try:
    #         self.db_session.commit()
    #     except SQLAlchemyError:
    #         self.db_session.rollback()
    #         log.error(msg='SQLAlchemyError', exc_info=True)
    #         raise Exception

    def do_write(self, data=None, status=True, error="", expect_time=None, send_mail=None):
        """这里做的事情比较简单，返回json对象给app或者机顶盒的时候，都是固定格式。
        status: bool(True/False),
        error: str('error message or ""'),
        result: dict('data object') or True.
        """
        if data is None:
            data = {}
        self.set_header("Content-Type", self.content_type or "application/json; charset=UTF-8")
        self.write(json.dumps(dict(status=status, error=error, result=data), ensure_ascii=False))

    @cached_property
    def config(self):
        """"""
        return Config(env=self.application.config)
