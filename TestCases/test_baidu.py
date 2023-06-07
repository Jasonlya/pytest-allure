# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:44
@Auth ： liangya
@File ：test_baidu.py
"""
from selenium import webdriver
from page.PageObject.BaiduPage import BaiduPage
from config.env import env_dict,current_url
from page.BasePage import BasePage as bp
from selenium.webdriver.common.by import By


class Testbaidu:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(env_dict[current_url])
        self.driver.maximize_window()

    def test_baidu(self):
        # BaiduPage = BaiduPage()
        # 读取页面元素
        KW = bp.kw
        # 点击
        bp.click(KW)
        # 输入
        bp.send_keys(KW, '我草泥马，傻逼女人')


if __name__ == '__main__':
    Testbaidu()