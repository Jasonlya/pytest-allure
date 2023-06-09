# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:06
@Auth ： liangya
@File ：BaiduPage.py
"""
from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class JcfwpzPage(BasePage):
    #页面url
    # url = 'http://192.168.20.164:8080/ywpt/courtmain.jsp'
    #页面元素
    yypzzx = (By.ID, '03')
    jcfwpz = (By.ID, '03_0301')
    #switch frame    //*[@id="capNav_cont"]/div[4]/iframe
    iframe1 = (By.XPATH, '//*[@id="capNav_cont"]/div[4]/iframe')
    input_fydm = (By.XPATH, '//*[@id="sfydm"]')
    input_fwid = (By.XPATH, '//*[@id="ssid"]')
    cxbt = (By.ID, 'btnSearch')
    def cx(self,input_fydm,input_fwid):
        """
        基础服务配置  查询   法院代码，服务ID
        :param input_fydm:
        :param input_fwid:
        :return:
        """
        JcfwpzPage = BasePage(self.driver)
        JcfwpzPage.click(self.yypzzx)
        JcfwpzPage.click(self.jcfwpz)
        time.sleep(2)
        JcfwpzPage.switch_to_frame(self.iframe1)
        time.sleep(3)
        JcfwpzPage.send_keys(self.input_fydm,input_fydm)
        JcfwpzPage.send_keys(self.input_fwid,input_fwid)
        JcfwpzPage.click(self.cxbt)

