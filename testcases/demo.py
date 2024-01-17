# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/15 22:32
@Auth ： liangya
@File ：demo.py
"""
import allure
import pytest
import logging as log


@allure.epic("服务平台")
@allure.feature("百度搜索")
@allure.story("百度搜索测试")
class TestBaidu:

    def test_baidu_search(self, web_driver):
        log.info("这是有一个测试demo")
        web_driver.get('http://192.168.13.95/main.html')
        log.info("页面打开完毕")
