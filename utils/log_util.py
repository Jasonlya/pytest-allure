# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/7 22:31
@Auth ： liangya
"""
import logging
import os
import time
from logging import handlers

from config.config_path import logs_dir


# 2.定义初始化日志函数
def set_log(filename):
    pass
    # ========定义日志器========
    logger = logging.getLogger()  # 初始化日志器对象
    logger.setLevel(logging.INFO)  # 设置日志器对应日志的格式
    # ========定义处理器========
    # 控制台处理器
    # 定义处理器
    sh = logging.StreamHandler()  # 控制台处理器
    sh.setLevel(logging.INFO)
    stime = time.strftime('%Y-%m-%d-%H-%M-%S_', time.localtime())
    log_file = os.path.join(logs_dir, stime+filename)
    fh = logging.handlers.TimedRotatingFileHandler(filename=log_file,  # 定义日志文件
                                                   when="D",  # 记录日志时间：按天
                                                   interval=1,  # 记录日志的频率 每天
                                                   backupCount=7,  # 保存日志的时间   7天
                                                   encoding="UTF-8"  # 记录日志的编码方式
                                                   )  # 文件处理器
    fh.setLevel(logging.INFO)
    # 定义格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 设置处理器的格式
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)