# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:06
@Auth ： liangya
@File ：BaiduPage.py
"""
from page.BasePage import BasePage as bp
from selenium.webdriver.common.by import By

class BaiduPage:

    sousuokuang = ('id="kw"')
    btn_summit = ('//*[@id="su"]')

    def search(self,sousuokuang,input_text):
        """
        搜素
        :param input_text:
        :return:
        """
        self.send_keys(self.sousuokuang,input_text)   #将字符输入到搜索框
        self.click(self.btn_summit)                   #点击提交按钮

