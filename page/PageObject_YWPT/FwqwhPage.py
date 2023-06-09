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

class FwqwhPage(BasePage):
    #页面url
    # url = 'http://192.168.20.164:8080/ywpt/courtmain.jsp'
    #页面元素
    jczy = (By.ID, '02')
    fwqwh = (By.ID, '02_0701')

    iframe1 = (By.XPATH, '//*[@id="capNav_cont"]/div[2]/iframe')
    xjbt = (By.ID, 'btnAdd')

    iframe2 = (By.XPATH, '//*[@id="layui-layer-iframe2"]')
    inputjdmc = (By.XPATH, '/html/body/form/table/tbody/tr[1]/td[2]/input')
    inputip = (By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/input')
    bcbt = (By.ID, 'btnSave')

    def xjfwq(self,input_jdmc,input_ip):
        """
        新建服务器 节点名称，ip
        :param input_jdmc:
        :param input_ip:
        :return:
        """
        FwqwhPage = BasePage(self.driver)
        FwqwhPage.click(self.jczy)
        FwqwhPage.click(self.fwqwh)
        time.sleep(3)
        FwqwhPage.switch_to_frame(self.iframe1)
        FwqwhPage.click(self.xjbt)
        time.sleep(3)
        FwqwhPage.switch_to_frame(self.iframe2)
        FwqwhPage.send_keys(self.inputjdmc,input_jdmc)
        FwqwhPage.send_keys(self.inputip,input_ip)
        FwqwhPage.click(self.bcbt)




