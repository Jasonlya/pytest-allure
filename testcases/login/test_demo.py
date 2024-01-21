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

@allure.epic("门户登录模块")
@allure.feature('门户登录功能')
@allure.story('登录成功')
@allure.step("步骤一")
def test_case_1():
    # 测试步骤和断言
    pass

@allure.epic("门户登录模块")
@allure.feature('门户登录功能')
@allure.story('登录成功')
@allure.step("步骤二")
def test_case_2():
    # 测试步骤和断言
    pass
