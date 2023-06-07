# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/8 1:19
@Auth ： liangya
@File ：main.py
"""

# import struct
import os

if __name__ == '__main__':
    # print(struct.calcsize("P") * 8)    #查看python的版本位数
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    print(ROOT_DIR)
