# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/31 0:44
@Auth ： liangya
@File ：env.py
"""

current_url = "uim"

env_dict = {
    "uim" : "http://192.168.20.164/8081/uim",
    "flow" : "http://192.168.20.164/8084/uim",
    "ywpt" : "http://192.168.20.164/8080/ywpt"
}


if __name__ == '__main__':
    print(env_dict[current_url])