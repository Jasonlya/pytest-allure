# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:44
@Auth ： liangya
@File ：test_baidu.py
"""
import logging
import os.path
import pytest
from page.PageObject_test.BaiduPage import BaiduPage
from config.env import env_dict,current_url
import time
from util.operationExcel import get_data_from_excel
from util.operationpath import get_path

class Testbaidu:
    # def setup_method(self):
    #     self.driver = webdriver.Chrome()
    #     self.baidu_page = BaiduPage(self.driver)
    # def teardown_method(self):
    #     self.driver.quit()

    @pytest.mark.parametrize("A,B,C",get_data_from_excel(os.path.join(get_path(),'./data/test_input.xlsx'),'Sheet1'))
    def test_baidu(self,browser,A,B,C):
        "'测试百度输入'"
        baidupage = BaiduPage(browser)
        baidupage.open()
        """隐式等待"""
        # self.driver.implicitly_wait(5)
        baidupage.search(A)
        assert current_url !='cc'

if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])   #, '-k', 'test_my_case or test_another_case'
