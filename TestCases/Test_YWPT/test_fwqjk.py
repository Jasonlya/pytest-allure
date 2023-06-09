# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：test_loginywpt.py
"""
import pytest
from page.PageObject_YWPT.FwqjkPage import FwqjkPage

@pytest.mark.skip("test not ready yet")
class Test_fwqjk:
    """测试登录功能"""

    def test_fwqjk_cx(self,loginywpt):
        """测试查询对应服务器的服务器监控信息是否存在"""
        fwqjk = FwqjkPage(loginywpt)
        # fwqwh.open()
        fwqjk.cx('192.168.13.126',input_fwid=None)


if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])   #, '-k', 'test_my_case or test_another_case'
