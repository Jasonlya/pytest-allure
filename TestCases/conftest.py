# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：conftest.py
"""
import pytest
from selenium import webdriver


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