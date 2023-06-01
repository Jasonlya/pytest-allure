# coding:utf-8

import unittest
import time

from uilib.login_page import Login_Page # 元素库
from Selenium_center import Log
from Selenium_center import TestCaseMore
from Selenium_center import Driver
from Selenium_center import By
from Selenium_center import DataDriver
from Selenium_center import Config

logger = Log()  # 创建日志记录对象,记录日志信息通过logger.info logger.error选择不同级别来记录

# 继承TestCaseMore 必填
class test01_login(TestCaseMore):

    @classmethod  # 执行整个TestCase中只调用一次setUp
    def setUpClass(cls):  # 案例初始化时执行 必填
        cls.driver = Driver(Config.project_url)  # 初始化驱动，指定浏览器类型并打开初始url

    @classmethod  # 执行整个TestCase中只调用一次tearDown
    def tearDownClass(cls):  # 案例结束时执行 必填
        cls.driver.quit()

    def test01_登录_01(self):  # 测试用例函数 类中至少要有一个
        logger.info("正在执行 test01_login_01")  # 记录日志，级别为info
        self.driver.maximize_window()
        self.driver.get_element(*Login_Page.用户名).clear()
        self.driver.get_element(*Login_Page.用户名).send_keys("ocp")
        self.driver.get_element(*Login_Page.密码).send_keys("000000")
        self.driver.get_element(*Login_Page.提交).click()
        time.sleep(2)
        logger.debug(self.driver.title)  # 记录日志，级别为debug
        self.driver.get_screen_shot()  # 截图，自动保存在log目录下
        # 断言
        print(self.checkElement(*(By.ID, "home$Menu")))     # 检查指定元素是否存在
        self.assertEqual(self.driver.title, "ORCA 虎鲸")   # 断言标题是否
        self.tearDownClass()


    def test01_登录_02(self):
        # 数据驱动测试
        self.login001()

    @DataDriver.run_data_from_excel(path=Config.project_dir + r"\Data\Login.xlsx")
    def login001(self, 登录名, 密码, 是否通过):
        print(登录名, 密码, 是否通过)
        self.setUpClass()
        self.driver.maximize_window()
        self.driver.get_element(*Login_Page.用户名).clear()
        self.driver.get_element(*Login_Page.用户名).send_keys(登录名)
        self.driver.get_element(*Login_Page.密码).send_keys(密码)
        self.driver.get_element(*Login_Page.提交).click()
        if 是否通过 == 'Y':
            self.driver.get_element(*(By.ID, "home$Menu"))
        self.tearDownClass()


# 案例也可单独调试
if __name__ == "__main__":
    unittest.main()
