# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/15 22:32
@Auth ： liangya
@File ：test_demo.py
"""
import allure
import pytest
import logging as log
from page_objects.baidu import  baidu
from common import base_page

@allure.feature('Feature 1')
@allure.story('Story 1')
@allure.title('Test Case 1')
def test_case_1():
    # 测试步骤和断言
    pass

@allure.feature('Feature 2')
@allure.story('Story 2')
@allure.title('Test Case 2')
def test_case_2():
    # 测试步骤和断言
    pass
