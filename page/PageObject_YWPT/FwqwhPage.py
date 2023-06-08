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

class FwqwhPage(BasePage):
    #页面url
    url = 'http://192.168.20.164:8080/ywpt/courtmain.jsp'
    def __init__(self,driver):
        super().__init__(driver)
        self.jczy = (By.ID,'02')
        self.fwqwh = (By.ID,'02_0701')
        self.xjbt = (By.ID,'btnAdd')
        self.inputjdmc = (By.XPATH,'/html/body/form/table/tbody/tr[1]/td[2]/input')
        self.inputip = (By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/input')
        self.bcbt = (By.ID,'btnSave')

    def open(self):
        "'打开页面'"
        self.driver.get(self.url)
    def xjfwq(self,input_jdmc,input_ip):
        """
        新建服务器 节点名称，ip
        :param input_jdmc:
        :param input_ip:
        :return:
        """
        BasePage.click(*self.jczy)
        BasePage.click(*self.fwqwh)
        BasePage.switch_to_frame()
        BasePage.click(*self.xjbt)
        BasePage.switch_to_frame()
        BasePage.switch_to_frame()
        BasePage.send_keys(*self.inputjdmc,input_jdmc)
        BasePage.send_keys(*self.inputip, input_ip)
        BasePage.click(*self.bcbt)


