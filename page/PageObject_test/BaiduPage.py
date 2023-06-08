# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:06
@Auth ： liangya
@File ：BaiduPage.py
"""
import os
from util.operationpath import get_path
from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

class BaiduPage(BasePage):
    #页面url
    url = 'http://baidu.com'

    sousuokuang = (By.ID,'kw')
    btn_summit = (By.XPATH,'//*[@id="su"]')
    def search(self,input_text):
        """
        搜索
        输入，点击
        :param input_text:
        :return:
        """
        """BasePage进行实例化"""
        BaiduPage = BasePage(self.driver)
        """将字符输入到搜索框"""
        BaiduPage.send_keys((By.ID,'kw'),input_text,5)
        """点击提交按钮"""
        BaiduPage.click((By.XPATH,'//*[@id="su"]'))



