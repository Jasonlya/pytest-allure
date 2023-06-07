# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:06
@Auth ： liangya
@File ：BaiduPage.py
"""
from page.BasePage import BasePage
from selenium.webdriver.common.by import By

class BaiduPage(BasePage):
    #页面url
    url = 'http://baidu.com'
    def __init__(self,driver):
        super().__init__(driver)
        self.sousuokuang = (By.ID,'kw')
        self.btn_summit = (By.XPATH,'//*[@id="su"]')
    def open(self):
        "'打开页面'"
        self.driver.get(self.url)
    def search(self,input_text):
        """
        搜索
        输入，点击
        :param input_text:
        :return:
        """
        # super().find_element(*self.sousuokuang).send_keys(input_text)
        self.driver.find_element(*self.sousuokuang).send_keys(input_text)  #将字符输入到搜索框
        self.driver.find_element(*self.btn_summit).click()                #点击提交按钮

