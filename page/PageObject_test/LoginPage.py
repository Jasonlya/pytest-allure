# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 22:42
@Auth ： liangya
@File ：LoginPageYWPT.py
"""

from selenium.webdriver.common.by import By
from page.BasePage import BasePage


class LoginPage:
    """登录页面"""

    # 页面 URL
    url = 'https://example.com/login'

    # 页面元素
    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    login_button = (By.ID, 'login-button')
    error_message = (By.ID, 'error-message')


    def login(self, username, password):
        """登录"""
        """实例化BasePage"""
        loginpage = BasePage(self.driver)
        """输入用户名"""
        loginpage.send_keys(*self.username_input,username)
        """输入密码"""
        loginpage.send_keys(*self.password_input,password)
        """点击登录"""
        loginpage.click(*self.login_button)


    def get_error_message(self):
        """获取错误提示信息"""
        return self.driver.find_element(*self.error_message).text
