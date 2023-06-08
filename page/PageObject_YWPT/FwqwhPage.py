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

if __name__ == '__main__':
    driver = webdriver.Chrome()
    test = FwqwhPage(driver=driver)
    driver.get('http://192.168.20.164:8080/ywpt/courtmain.jsp')
    driver.delete_all_cookies()
    time.sleep(5)
    driver.maximize_window()
    time.sleep(5)
    #{'name' : 'foo', 'value' : 'bar'}
    driver.add_cookie({'JSESSIONID' : 'D303AF4736589995E4A80EECED31B6EB'})
    time.sleep(3)
    driver.refresh()
    time.sleep(5)


