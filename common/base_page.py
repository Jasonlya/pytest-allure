# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:48
@Auth ： liangya
@File ：base_page.py
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
)
import logging as logger
import os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UISTYLE = "background: green; border: 2px solid red;"


class BasePage:
    def __init__(self, driver):
        self.driver = webdriver.Chrome()

    def open(self, url):
        "'打开页面'"
        # self.driver.get(self.url)
        self.driver.get(url)

    #
    def find_element(self, locator, timeout=10):
        """定位单个元素"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].setAttribute('uistyle',arguments[1]);", element, UISTYLE)
        return element

    def wait_for_element(self, locator, timeout=10):
        """进行元素等待"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=10):
        """定位元素元组"""
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        self.driver.execute_script("arguments[0].setAttribute('uistyle',arguments[1]);", elements, UISTYLE)
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

    def select_option_by_text(self, locator, text, timeout=10):
        """根据下拉框的文本值进行选择"""
        try:
            element = self.find_element(locator, timeout)
            Select(element).select_by_visible_text(text)
        except Exception as e:
            print('下拉框选择失败：' + e)

    def select_option_by_index(self, locator, index, timeout=10):
        """根据下拉框的索引进行选择"""
        try:
            element = self.find_element(locator, timeout)
            Select(element).select_by_index(index)
        except Exception as e:
            print('下拉框选择失败：' + e)

    def select_option_by_value(self, locator, value, timeout=10):
        """根据下拉框的value值进行选择"""
        try:
            element = self.find_element(locator, timeout)
            Select(element).select_by_value(value)
        except Exception as e:
            print('下拉框选择失败：' + e)

    def take_screenshot(self, filename):
        """截屏"""
        self.driver.save_screenshot(filename)

    def take_screenshot_x_y(self, locator, filename):
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

    # 切换窗口
    def switch_window(self, filepath):
        time.sleep(3)
        try:
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[-1])
            self.log.info('切换窗口成功')
        except Exception as e:
            self.logger.error(f'切换窗口失败，报错信息为{e}')
            raise Exception(f'切换窗口失败，报错信息为{e}')

    '''浏览器事件-前进'''

    def go_forward(self):
        try:
            self.driver.forward()
        except Exception as e:
            logging.error("无法前进，当前页面可能是历史记录的最后一页。" + str(e))
            # 失败截图
            self.save_screen("go_forward")
            raise

    '''浏览器事件-后退'''

    def go_back(self):

        try:
            self.driver.back()
        except:
            logging.error(f"浏览器事件-错误")
            # 失败截图
            self.save_screen("go_back")
            raise
