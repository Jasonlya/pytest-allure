# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:44
@Auth ： liangya
@File ：run.py
"""
import pytest
import os
from util import log_util

if __name__ == '__main__':
    # 使用日志： 请使用info或以上级别记录日志
    # log_util.set_log("discover.log")
    pytest.main(["-vs", "--alluredir", "outputs/allure/temp_jsonreport", "--clean-alluredir"])
    os.system("allure generate outputs/allure/temp_jsonreport -o outputs/allure/html --clean")
