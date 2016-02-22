# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'TT'

__release__ = 'RELEASE'


class Config(object):
    """"""

    db_pool = dict(
        common=0,
    )

    def __init__(self, env=None):
        """
        初始化配置文件
        """
        if env == __author__:
            self.tt_conf()
        elif env == __release__:
            self.release_conf()
        else:
            self.debug = True
            # mysql config
            self.mysql_user = 'root'
            self.mysql_host = '127.0.0.1'
            self.mysql_password = '123qwe'
            self.mysql_db = 'tt-blog'
            self.mysql_port = '3306'
            self.mysql_echo = False
            # redis config
            self.redis_host = '127.0.0.1'
            self.redis_port = '6379'
            self.redis_password = ''

    def tt_conf(self):
        """
        TT config
        """
        self.debug = False
        # mysql config
        self.mysql_user = 'root'
        self.mysql_host = '127.0.0.1'
        self.mysql_password = '123qwe'
        self.mysql_db = 'tt-blog'
        self.mysql_port = '3306'
        self.mysql_echo = False
        # redis config
        self.redis_host = '127.0.0.1'
        self.redis_port = '6379'
        self.redis_password = ''

    def release_conf(self):
        """
        release config
        """
        self.debug = False
        # mysql config
        self.mysql_user = 'root'
        self.mysql_host = '127.0.0.1'
        self.mysql_password = '123qwe'
        self.mysql_db = 'tt-blog'
        self.mysql_port = '3306'
        self.mysql_echo = False
        # redis config
        self.redis_host = '127.0.0.1'
        self.redis_port = '6379'
        self.redis_password = ''
