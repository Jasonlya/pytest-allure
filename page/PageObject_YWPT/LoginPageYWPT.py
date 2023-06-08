# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 22:42
@Auth ： liangya
@File ：LoginPageYWPT.py
"""

from selenium.webdriver.common.by import By
from page.BasePage import BasePage
from util.opeartionYzm import operationyzm
from selenium import webdriver
import time

class LoginPageYWPT(BasePage):
    """登录页面"""

    # 页面 URL
    url = 'http://192.168.20.164:8080/ywpt'

    # 页面元素
    # username_input = (By.ID, 'username')
    # password_input = (By.ID, 'password')
    # yzm_input = (By.ID, 'captcha')
    # login_button = (By.ID, 'dl')
    # error_message = (By.ID, 'error-message')
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.yzmimg = (By.ID,'captchaImg')
        self.yzm_input = (By.ID, 'captcha')
        self.login_button = (By.ID, 'dl')
    def open(self):
        """打开页面"""
        self.driver.get(self.url)

    def login(self, username, password):
        """登录"""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        """验证码处理，返回yzm_input"""
        img = self.driver.find_element(*self.yzmimg)
        # rect = img.getRect()
        # print(rect)
        img.screenshot('./yzm.png')
        yzm_input = operationyzm('./yzm.png')
        print(yzm_input)
        time.sleep(5)
        """输入验证码"""
        self.driver.find_element(*self.yzm_input).send_keys(yzm_input)
        """登录"""
        time.sleep(5)
        self.driver.find_element(*self.login_button).click()
        time.sleep(5)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    test = LoginPageYWPT(driver=driver)
    test.open()
    driver.maximize_window()
    time.sleep(5)
    test.login('admin','Tdh@123456')