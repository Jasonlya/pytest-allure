# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/15 22:32
@Auth ： liangya
@File ：baidu_test.py
"""
import allure
import pytest
import logging as log
from page_objects.baidu import  baidu
from common import base_page

@allure.epic("服务平台")
@allure.feature("百度搜索")
@allure.story("百度搜索测试")
class TestBaidu:
    # @pytest.fixture("dc")
    def test_baidu_search(self):
        log.info("这是有一个测试demo")
        baidu.search(self,'test')
        # baidu.
        # self.open()
        # self.search("Python")
        # self.assert_title("Python_百度搜索")
        # self.assert_contains("Python")
        # self.save_screenshot()
