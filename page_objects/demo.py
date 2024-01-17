# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/15 22:31
@Auth ： liangya
@File ：demo.py
"""
import logging

from page_locations import demo
from common.base_page import BasePage


class baidu(BasePage):

    def search(self, text):
        logging.info("搜索内容：{}".format(text))
        BasePage.open(self,'www.baidu.com')
        # self.click()
