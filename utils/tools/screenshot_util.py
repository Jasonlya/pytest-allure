# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/25 21:36
@Auth ： liangya
@File ：screenshot_util.py
"""
import os.path

from selenium import webdriver
# from config import globalparam
import sys
from config.config_path import screenshots_dir

sys.path.append('/home/selenium_python')


class Screen(object):
    """截图功能装饰器"""

    def __init__(self, driver):
        self.driver = driver

    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except:
                import time
                nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
                file_name = '%s.jpg' % nowTime
                file_path = os.path.join(screenshots_dir, "\\", file_name)
                self.driver.get_screenshot_as_file(file_path)
                raise

        return inner
