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
    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    yzm_input = (By.ID, 'captcha')
    login_button = (By.ID, 'dl')
    # error_message = (By.ID, 'error-message')
    def login(self, username, password):
        """登录"""
        """实例化BasePage对象"""
        loginpage = BasePage(self.driver)
        """输入用户名"""
        loginpage.send_keys(*self.username_input,username)
        """输入密码"""
        loginpage.send_keys(*self.password_input,password)
        """验证码处理，返回yzm_input"""
        img = self.driver.find_element(*self.yzmimg)
        # rect = img.getRect()
        # print(rect)
        img.screenshot('./yzm.png')
        yzm = operationyzm('./yzm.png')
        print(yzm)
        time.sleep(5)
        """输入验证码"""
        loginpage.send_keys(*self.yzm_input,yzm)
        """点击登录"""
        loginpage.click(*self.login_button)
        time.sleep(5)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    test = LoginPageYWPT(driver)
    test.open()
    time.sleep(5)
    test.login('admin','Tdh@123456')