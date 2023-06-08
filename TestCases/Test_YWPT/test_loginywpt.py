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

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.TestLogin = LoginPageYWPT(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_loginywpt(self):
        """测试登录成功"""
        self.TestLogin.open()
        self.TestLogin.login('admin', 'Tdh@123456',operationyzm(image=r'F:\PycharmProjects\pytest-allure\pytest-allure\util\test.png'))
        assert self.driver.current_url != 'http://192.168.20.164:8080/ywpt/courtmain.jsp'

    # def test_login_failure(self):
    #     """测试登录失败"""
    #     self.login_page.open()
    #     self.login_page.login('user', 'wrong-password')
    #     self.assertEqual(self.login_page.get_error_message(), '用户名或密码错误')

if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])   #, '-k', 'test_my_case or test_another_case'
