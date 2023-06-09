# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:45
@Auth ： liangya
@File ：test_loginywpt.py
"""
import pytest
from page.PageObject_YWPT.SjkfwglPage import SjkfwglPage
class TestSjkfwq:
    """测试登录功能"""

    def test_sjkfwq_add(self,loginywpt):
        """测试添加数据库服务器"""
        sjkfwq_add = SjkfwglPage(loginywpt)
        sjkfwq_add.sjkfwq_add('uitest',2,'192.168.66.11','5001','test','uitest','root','123456','1')

if __name__ == '__main__':
    pytest.main(['-s', '-v', __file__])   #, '-k', 'test_my_case or test_another_case'
