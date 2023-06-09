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

class SjkfwglPage(BasePage):
    #页面元素
    jczy = (By.ID, '02')
    sjkf = (By.ID, '02_0201')

    iframe1 = (By.XPATH, '//*[@id="capNav_cont"]/div[2]/iframe')
    xzbtn = (By.ID, 'btnAdd')

    iframe2 = (By.XPATH, '//*[@id="layui-layer-iframe2"]')
    inputfwqmc = (By.XPATH, '/html/body/form/table/tbody/tr[1]/td[2]/input')
    """下拉框  两次定位；通过select方法"""
    inuputsjk = (By.CLASS_NAME, 'select_showbox')
    selectsjk = (By.XPATH, '//*[@id="selectedId"]')   #/html/body/form/table/tbody/tr[2]/td[2]/div/ul  /html/body/form/table/tbody/tr[2]/td[2]/div/div
    inputMYSQL = (By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/div/ul/li[3]')
    inputORCLE = (By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/div/ul/li[2]')

    inputip = (By.NAME, 'ipaddr')
    inputport = (By.NAME, 'port')
    inputfwqsl = (By.NAME, 'oraclesid')
    inputzfj = (By.NAME, 'charset')
    inputyh = (By.NAME, 'sa')
    inputpwd = (By.NAME, 'sapass')
    inputpxh = (By.NAME, 'pxh')
    bcbt = (By.XPATH, '//*[@id="btnsave"]')

    #页面行为
    def sjkfwq_add(self,inputfwqmc,inputsjk,inputip,inputport,inputfwqsl,inputzfj,inputyh,inputpwd,inputpxh):
        """
        新增数据库服务器 服务器名称，数据库，ip，端口号，实例，字符集，账号，密码，排序号
        :param inputfwqmc:
        :param inputsjk:
        :param inputip:
        :param inputport:
        :param inputfwqsl:
        :param inputzfj:
        :param inputyh:
        :param inputpwd:
        :param inputpxh:
        :return:
        """
        xzsjkfwq = BasePage(self.driver)
        xzsjkfwq.click(self.jczy)
        xzsjkfwq.click(self.sjkf)
        time.sleep(1)

        xzsjkfwq.switch_to_frame(self.iframe1)
        xzsjkfwq.click(self.xzbtn)
        time.sleep(1)

        xzsjkfwq.switch_to_frame(self.iframe2)
        time.sleep(1)
        xzsjkfwq.send_keys(self.inputfwqmc,inputfwqmc)
        time.sleep(1)
        """下拉框处理-两次定位"""
        xzsjkfwq.click(self.inuputsjk)
        xzsjkfwq.click(self.inputORCLE)
        # xzsjkfwq.select_option_by_text(self.selectsjk,inputsjk)

        xzsjkfwq.send_keys(self.inputip, inputip)
        xzsjkfwq.send_keys(self.inputport, inputport)
        xzsjkfwq.send_keys(self.inputfwqsl, inputfwqsl)
        xzsjkfwq.send_keys(self.inputzfj, inputzfj)
        xzsjkfwq.send_keys(self.inputyh, inputyh)
        xzsjkfwq.send_keys(self.inputpwd, inputpwd)
        xzsjkfwq.send_keys(self.inputpxh, inputpxh)
        time.sleep(2)
        xzsjkfwq.click(self.bcbt)


