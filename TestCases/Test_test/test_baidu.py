# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:44
@Auth ： liangya
@File ：test_baidu.py
"""
import pytest
from selenium import webdriver
from page.PageObject_test.BaiduPage import BaiduPage
from config.env import env_dict,current_url
import time


class Testbaidu:
    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.baidu_page = BaiduPage(self.driver)
    # def tearDown(self):
    #     self.driver.quit()
    def test_baidu(self,browser):
        "'测试百度输入'"
        self.baidu_page = BaiduPage(self.driver)
        self.baidu_page.open()
        self.driver.maximize_window()
        time.sleep(5)    #强制等待
        self.driver.implicitly_wait(5)  #隐式等待
        self.baidu_page.search('测试水是生是死')
        assert current_url !='cc'


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])   #, '-k', 'test_my_case or test_another_case'
