# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:16
@Auth ： liangya
@File ：conf.py
"""

DATA_Path = './data'         #参数化文件的路径
select_browser = 'chrome'    #选择不同的浏览器进行测试   'fiefox','chrome'
env = {
    "ywpt":"http://192.168.20.164:8080/ywpt",
    "uim":"http://192.168.20.164:8081/uim",
    "flow":"http://192.168.20.164:8084/flow"
}

if __name__ == '__main__':
    print(env["ywpt"])