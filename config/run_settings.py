# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/4 23:16
@Auth ： liangya
@File ：run_settings.py
"""

ENV_VARS = {
    "common": {
        "报告标题": "UI自动化测试报告",
        "项目名称": "审判系统test",
    },
    "test": {
        # 示例测试环境及示例测试账号
        "host": "https://127.0.0.1:71/portal"
    },
    "live": {
        "host": "https://www.gitlink.org.cn",
    }
}



# redis配置
REDIS_CONFIG = {
    "host": "192.168.0.151",
    # "host": "127.0.0.1",
    "port": "6379",
    "password": "",
    "db": 2
}

# ------------------------------------ pytest相关配置 ----------------------------------------------------#
class RunConfig:
    """
    运行测试配置
    """
    # 配置浏览器驱动类型(chromium, firefox, webkit)。
    browser = ["chromium"]

    # 运行模式（headless, headed）
    mode = "headed"

    # 窗口大小
    """
    playwright 默认启动的浏览器窗口大小是1280x720， 我们可以通过设置no_viewport参数来禁用固定的窗口大小 ，no_viewport 禁用窗口大小。
    """
    # 这个标识根据具体尺寸设置窗口大小
    window_size = {"width": 1920, "height": 1080}

    # 浏览器页面
    page = None

    # 失败重跑次数
    rerun = 0

    # 失败重跑间隔时间
    reruns_delay = 5

    # 当达到最大失败数，停止执行
    max_fail = "10"
