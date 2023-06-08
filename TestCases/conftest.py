# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：conftest.py
"""
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def login(webdriver):
    # 在这里进行登录操作
    yield
    # 在这里进行退出操作

@pytest.fixture(scope="session")
def db():
    # 数据库连接操作
    yield
    # 断开数据库连接操作

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="environment.properties: dev or prod")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture()
def browser():
    # 启动浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # 关闭浏览器
    driver.quit()
@pytest.fixture()
def loginywpt():
    driver =webdriver.Chrome()
    driver.maximize_window()
    """执行登录"""
    driver.get("http://192.168.20.164:8080/ywpt")
    driver.find_element(By.ID, 'username').send_keys('admin')
    driver.find_element(By.ID, 'password').send_keys('Tdh@123456')
    """验证码获取"""
    # driver.find_element()
    time.sleep(8)
    """解析为字符串"""
    # yzm='123'
    # driver.find_element(By.ID, 'captcha').send_keys(yzm)
    driver.find_element(By.XPATH, '//*[@id="dl"]').click()
    time.sleep(5)
    """返回浏览器对象"""
    yield driver

    """关闭浏览器"""
    driver.quit()