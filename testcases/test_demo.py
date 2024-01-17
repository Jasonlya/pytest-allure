# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/15 22:32
@Auth ： liangya
@File ：test_demo.py
"""
import allure
import pytest
import logging as log
from common import base_page

@allure.epic("审判系统")
@allure.feature('门户登录模块')
@allure.story('门户登录功能')
@allure.suite("登录成功")
@allure.title('登录成功2')
@allure.title("步骤一")
def test_case_1():
    # 测试步骤和断言
    pass

@allure.epic("审判系统")
@allure.feature('门户登录模块')
@allure.story('门户登录功能')
@allure.title('登录失败')
@allure.step("步骤二")
def test_case_2():
    # 测试步骤和断言
    pass
