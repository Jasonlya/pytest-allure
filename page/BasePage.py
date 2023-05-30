# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:48
@Auth ： liangya
@File ：BasePage.py
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element

    def find_elements(self, locator, timeout=10):
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return elements

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def send_keys(self, locator, keys, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text

    def get_title(self):
        return self.driver.title
