# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：conftest.py
"""
import pytest

@pytest.fixture
def login():
    # 登录操作
    yield
    # 退出登录操作

@pytest.fixture(scope="session")
def db():
    # 数据库连接操作
    yield
    # 断开数据库连接操作

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="environment: dev or prod")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")
