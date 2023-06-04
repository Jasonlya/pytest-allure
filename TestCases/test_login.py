# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：test_login.py
"""
import allure
from page.LoginPage import LoginPage
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

class Test_testlogin():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.qq.com/')
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        self.login_page.enter_username('')
        self.login_page.enter_password('')
        self.login_page.click_login_button()
        assert '' in self.driver.page_source

if __name__ == '__main__':
    Test_testlogin()