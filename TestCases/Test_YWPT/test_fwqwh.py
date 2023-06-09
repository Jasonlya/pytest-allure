# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：test_loginywpt.py
"""
import pytest
from selenium import webdriver
from page.PageObject_YWPT.FwqwhPage import FwqwhPage
from util.opeartionYzm import operationyzm
class TestFwqwh:
    """测试登录功能"""

    def test_fqwh_add(self,loginywpt):
        """测试登录成功"""
        fwqwh = FwqwhPage(loginywpt)
        # fwqwh.open()
        fwqwh.xjfwq('192.168.测试名称','192.168.111.233')

if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])   #, '-k', 'test_my_case or test_another_case'
