# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：test_login1.py
"""
from page.PageObject_test.LoginPage import LoginPage
from selenium import  webdriver

# with allure.feature():
# class Test_test:
#     def test_add(self):
#         assert 1+2==3
#
#     def test_sub(self):
#         with allure.step("测试allure插件函数"):
#             assert 1==1
#
#     def test_aa(self):
#         ab=["sss","bbb"]
#         a="sss"
#         assert a in ab

import unittest
from selenium import webdriver
from page.PageObject_test.LoginPage import LoginPage

class TestLogin():
    """测试登录功能"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        """测试登录成功"""
        self.login_page.open()
        self.login_page.login('user', 'password')
        self.assertEqual(self.driver.current_url, 'https://example.com/home')

    def test_login_failure(self):
        """测试登录失败"""
        self.login_page.open()
        self.login_page.login('user', 'wrong-password')
        self.assertEqual(self.login_page.get_error_message(), '用户名或密码错误')
