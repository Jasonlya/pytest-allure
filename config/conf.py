# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:16
@Auth ： liangya
@File ：conf.py
"""
# 参数化文件的路径
DATA_Path = './data'

#选择不同的浏览器进行测试   'fiefox','chrome'
select_browser = 'chrome'

#运行环境,不同的测试用例文件夹下Test_XX会自动获取xx对应的url
env = {
    "ywpt":"http://192.168.20.164:8080/ywpt",
    "uim":"http://192.168.20.164:8081/uim",
    "flow":"http://192.168.20.164:8084/flow"
}
#是否以无头的方式运行  1 无头运行 0 正常浏览器运行
headless = 0

#运行窗口的大小   1--1920*1080  2--1366*768  0--最大化
#默认用例基本上兼容1920*1080和最大化(可通过driver.get_window_size获取当前最大化窗口大小)     1366*768由于元素定位三要素需要对页面滚动进行兼容
WindowSize = 0

if __name__ == '__main__':
    print(env["ywpt"])