# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：conftest.py
"""
import time
# from config.conf import select_browser, headless, WindowSize
import pytest
from selenium import webdriver
# from config.conf import env


@pytest.fixture(scope='function')
def login(webdriver):
    # 在这里进行登录操作
    yield
    # 在这里进行退出操作


# # 解决卡顿
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

@pytest.fixture(scope="session")
def db():
    # 数据库连接操作
    yield
    # 断开数据库连接操作


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="environment.properties: dev or prod")


# @pytest.fixture(scope="session")
# def env(request):
#     return request.config.getoption("--env")


# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()


@pytest.fixture(scope='session')
def web_driver():
    driver = webdriver.Chrome()
    # driver = open_browser('chrome')
    driver.maximize_window()
    # driver.implicitly_wait(10)
    yield driver
    driver.quit()
#
# @pytest.fixture()
# def browser():
#     # 启动浏览器
#     try:
#         if select_browser == 'chrome':
#             if headless == 1:
#                 """无头浏览器运行"""
#                 options = webdriver.ChromeOptions()
#                 options.add_argument('--headless')
#                 driver = webdriver.Chrome(options=options)
#             else:
#                 """正常浏览器加载"""
#                 driver = webdriver.Chrome()
#         if select_browser == 'fiefox':
#             if headless == 1:
#                 """无头浏览器运行"""
#                 options = webdriver.FirefoxOptions()
#                 options.add_argument('--headless')
#                 driver = webdriver.Firefox(options=options)
#             else:
#                 """正常浏览器加载"""
#                 driver = webdriver.Fiefox()
#         if WindowSize == 1:
#             driver.set_window_size(1920 * 1080)
#         elif WindowSize == 2:
#             driver.set_window_size(1366, 768)
#         else:
#             """最大化窗口"""
#             driver.maximize_window()
#     except:
#         print('select browser arise error')
#
#     yield driver
#     # 关闭浏览器
#     driver.quit()

#
# @pytest.fixture()
# def loginywpt():
#     try:
#         if select_browser == 'chrome':
#             if headless == 1:
#                 """无头浏览器运行"""
#                 options = webdriver.ChromeOptions()
#                 options.add_argument('--headless')
#                 driver = webdriver.Chrome(options=options)
#             else:
#                 # """正常浏览器加载--清缓存"""
#                 # options = webdriver.ChromeOptions()
#                 # options.add_argument('--disable-cache')
#                 # driver = webdriver.Chrome(options=options)
#                 # """正常浏览器加载--不清缓存"""
#                 driver = webdriver.Chrome()
#         if select_browser == 'fiefox':
#             if headless == 1:
#                 """无头浏览器运行"""
#                 options = webdriver.FirefoxOptions()
#                 options.add_argument('--headless')
#                 driver = webdriver.Firefox(options=options)
#             else:
#                 """正常浏览器加载"""
#                 driver = webdriver.Fiefox()
#         if WindowSize == 1:
#             driver.set_window_size(1920 * 1080)
#         elif WindowSize == 2:
#             driver.set_window_size(1366, 768)
#         else:
#             """最大化窗口"""
#             driver.maximize_window()
#     except:
#         print('select browser arise error')
#     """执行登录"""
#     driver.get(env["ywpt"])
#     driver.find_element(By.ID, 'username').send_keys('admin')
#     driver.find_element(By.ID, 'password').send_keys('Tdh@123456')
#     """验证码获取"""
#     # driver.find_element()
#     time.sleep(8)
#     """解析为字符串"""
#     # yzm='123'
#     # driver.find_element(By.ID, 'captcha').send_keys(yzm)
#     driver.find_element(By.XPATH, '//*[@id="dl"]').click()
#     time.sleep(5)
#     """返回浏览器对象"""
#     yield driver
#
#     """关闭浏览器"""
#     driver.quit()
# # 钩子函数，实现异常截图
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport():
#     out = yield  # yield ==》用例执行结果result对象
#     report = out.get_result()  # report ==》用例执行结果的report对象
#     """
#         report对象属性：when,nodeid,outcome
#         when（setup, call, teardown） 用例执行阶段
#         nodeid   用例名字
#         outcome（passed,failed）   用例执行结果
#     """
#
#     if report.when == "call":
#         # 获取用例call阶段执行结果为失败的情况
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # 添加allure报告截图
#             with allure.step("用例执行失败截图==="):
#                 # allure添加附件--》allure.attach（源文件、文件名、文件类型）