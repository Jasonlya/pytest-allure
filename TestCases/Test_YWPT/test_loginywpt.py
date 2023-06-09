# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：test_loginywpt.py
"""
import pytest
from selenium import webdriver
from page.PageObject_YWPT.LoginPageYWPT import LoginPageYWPT
from util.opeartionYzm import operationyzm
class TestLogin:
    """测试登录功能"""
    def test_loginywpt_success(self,browser):
        """测试登录成功"""
        login = LoginPageYWPT(browser)
        login.open()
        login.login('admin', 'Tdh@123456')
        assert browser.current_url == 'http://192.168.20.164:8080/ywpt/courtmain.jsp'

    def test_login_failure(self,browser):
        """测试登录失败"""
        login = LoginPageYWPT(browser)
        login.open()
        login.login('admin', 'Tdh@123456')
        assert browser.current_url == 'http://192.168.20.164:8080/ywpt/courtmain.jsp'

if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])   #, '-k', 'test_my_case or test_another_case'
