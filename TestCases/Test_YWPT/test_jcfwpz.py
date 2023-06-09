# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：test_loginywpt.py
"""
import pytest
from page.PageObject_YWPT.JcfwpzPage import JcfwpzPage

class Test_jcfwpz:
    """测试登录功能"""

    def test_jcfwpz_cx(self,loginywpt):
        """测试查询服务器配置"""
        jcfwpz = JcfwpzPage(loginywpt)
        # fwqwh.open()
        jcfwpz.cx('320100',input_fwid=None)


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])   #, '-k', 'test_my_case or test_another_case'
