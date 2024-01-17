# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/7 22:31
@Auth ： liangya
"""
import os
import yaml


def getyaml(file_name):
    absolute_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\datas' + '\\'  # 获取日志文件夹的就绝对路径
    ymalname = absolute_path + file_name
    with open(ymalname, 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    return result
