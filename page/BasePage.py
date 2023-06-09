# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:48
@Auth ： liangya
@File ：BasePage.py
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def open(self):
        "'打开页面'"
        self.driver.get(self.url)
    def find_element(self, locator, timeout=10):
        """定位单个元素"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element
    def wait_for_element(self, locator, timeout=10):
        """进行元素等待"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    def find_elements(self, locator, timeout=10):
        """定位元素元组"""
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return elements

    def click(self, locator, timeout=10):
        """点击"""
        element = self.find_element(locator, timeout)
        element.click()

    def send_keys(self, locator, keys, timeout=10):
        """输入值"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    def get_text(self, locator, timeout=10):
        """获取元素文本"""
        element = self.find_element(locator, timeout)
        return element.text

    def get_title(self):
        """获取页面标题"""
        return self.driver.title

    def select_option_by_text(self,locator,text,timeout=10):
        """根据下拉框的文本值进行选择"""
        try:
            element = self.find_element(locator,timeout)
            Select(element).select_by_visible_text(text)
        except Exception as e:
            print('下拉框选择失败：'+e)

    def select_option_by_index(self,locator,index,timeout=10):
        """根据下拉框的索引进行选择"""
        try:
            element = self.find_element(locator,timeout)
            Select(element).select_by_index(index)
        except Exception as e:
            print('下拉框选择失败：'+e)

    def select_option_by_value(self,locator,value,timeout=10):
        """根据下拉框的value值进行选择"""
        try:
            element = self.find_element(locator,timeout)
            Select(element).select_by_value(value)
        except Exception as e:
            print('下拉框选择失败：'+e)

    def take_screenshot(self, filename):
        """截屏"""
        self.driver.save_screenshot(filename)

    def take_screenshot_x_y(self,locator,filename):
        """截取对应元素的图"""
        element = self.driver.find_element()

    byDic = {'id': By.ID, 'name': By.NAME, 'xpath': By.XPATH, 'css': By.CSS_SELECTOR}
    outTime = 10
    def switch_to_frame(self, locator):
        """
        判断frame是否存在，存在就跳到frame
        :param by:
        :param locator:
        :return:
        """
        print('\ninfo:switching to iframe "{}"'.format(locator))
        try:
            WebDriverWait(self.driver, self.outTime). \
                until(EC.frame_to_be_available_and_switch_to_it(locator))
        except TimeoutException as t:
            print('\nerror: found "{}" timeout！切换frame失败'.format(locator), t)


    def switch_to_default_frame(self):
        """返回默认的frame"""
        print('\ninfo:switch back to default iframe')
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(e)

    def get_alert_text(self):
        """获取alert的提示信息"""
        alert = self.is_alert()
        if alert:
            return alert.text
        else:
            return None
