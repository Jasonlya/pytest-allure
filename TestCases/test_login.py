# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：test_login.py
"""
import allure

# with allure.feature():
class Test_test:
    def test_add(self):
        assert 1+2==3

    def test_sub(self):
        with allure.step("测试allure插件函数"):
            assert 1==1

    def test_aa(self):
        ab=["sss","bbb"]
        a="sss"
        assert a in ab


if __name__ == '__main__':
    pass