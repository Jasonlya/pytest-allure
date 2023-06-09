# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:06
@Auth ： liangya
@File ：BaiduPage.py
"""
from page.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class FwqjkPage(BasePage):
    #页面url
    # url = 'http://192.168.20.164:8080/ywpt/courtmain.jsp'
    #页面元素
    jkzx = (By.ID, '05')
    fwqjk = (By.ID, '05_0501')

    iframe1 = (By.XPATH, '//*[@id="capNav_cont"]/div[3]/iframe')
    input_fwq = (By.XPATH,'/html/body/div[1]/div[1]/table/tbody/tr/td[2]/div/div/input')
    input_zt = (By.XPATH,'/html/body/div[1]/div[1]/table/tbody/tr/td[5]/div/div/input')
    cxbt = (By.XPATH, '/html/body/div[1]/div[1]/table/tbody/tr/td[6]/a[1]')

    def fwqjk_cx(self,input_fwq,input_zt):
        """
        新建服务器 节点名称，ip
        :param input_jdmc:
        :param input_ip:
        :return:
        """
        fwqjk_cx = BasePage(self.driver)
        fwqjk_cx.click(self.jkzx)
        fwqjk_cx.click(self.fwqjk)
        time.sleep(3)
        fwqjk_cx.switch_to_frame(self.iframe1)
        fwqjk_cx.click(self.xjbt)
        time.sleep(3)
        fwqjk_cx.switch_to_frame(self.iframe2)
        fwqjk_cx.send_keys(self.input_fwq,input_fwq)
        fwqjk_cx.send_keys(self.input_zt,input_zt)
        fwqjk_cx.click(self.bcbt)




