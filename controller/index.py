# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'TT'

from controller.base_controller import BaseController
import logging as log


class Index(BaseController):
    """
    index page
    """

    url = r'/?'

    def get(self, *args, **kwargs):
        """"""
        # self.write('HELLO WORLD!')
        self.render('index.html')

    def post(self, *args, **kwargs):
        """"""
        return self.get(*args, **kwargs)

