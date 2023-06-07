# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/8 2:21
@Auth ： liangya
@File ：operationpath.py
"""
import os

def get_path():
    """
    获取固定某上层路径
    :return: 路径
    """
    path = os.getcwd()
    path1, path2 = os.path.split(path)
    for i in range(9):
        if path2 != 'pytest-allure':
            path1, path2 = os.path.split(path1)
            continue
        else:
            path = os.path.join(path1, path2)
            break
    return path
