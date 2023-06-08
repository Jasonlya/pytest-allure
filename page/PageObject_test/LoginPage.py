# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 22:42
@Auth ： liangya
@File ：LoginPageYWPT.py
"""

from selenium.webdriver.common.by import By

class LoginPage:
    """登录页面"""

    # 页面 URL
    url = 'https://example.com/login'

    # 页面元素
    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    login_button = (By.ID, 'login-button')
    error_message = (By.ID, 'error-message')

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """打开页面"""
        self.driver.get(self.url)

    def login(self, username, password):
        """登录"""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        """获取错误提示信息"""
        return self.driver.find_element(*self.error_message).text
