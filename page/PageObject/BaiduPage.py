# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:06
@Auth ： liangya
@File ：BaiduPage.py
"""
from page.BasePage import BasePage as bp

class BaiduPage:
    #读取页面元素
    KW = bp.find_element("kw")
    #点击
    bp.click(KW)
    #输入
    bp.send_keys(KW,'我草泥马，傻逼女人')
