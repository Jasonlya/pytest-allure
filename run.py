# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:44
@Auth ： liangya
@File ：run.py
"""

# import pytest
# import os
# from utils import log_util

# if __name__ == '__main__':
#     # 使用日志： 请使用info或以上级别记录日志
#     log_util.set_log("test.log")
#     pytest.main(["-vs", "--alluredir", "outputs/allure/temp_jsonreport", "--clean-alluredir", ""])
#     os.system("allure generate  outputs/allure/temp_jsonreport -o outputs/allure/html --clean")
#
# 标准库导入
import os
import argparse
import logging as logger
from utils import log_util
import pytest
# 本地模块导入
from config.run_settings import RunConfig, ENV_VARS
from config.config_path import ALLURE_RESULTS_DIR, ALLURE_HTML_DIR, CONF_DIR
from common.global_var import GLOBAL_VARS
from utils.report_utils.re_report import generate_allure_report
from utils.tools.http_server import HttpServer


def run(**kwargs):
    try:
        # ------------------------ 捕获日志----------------------------
        # capture_logs(level=LOG_LEVEL, filename=os.path.join(LOG_DIR, "service.log"))
        log_util.set_log("test.log")
        logger.info("""
             _ _ _ _ __   _ _ _ _ _     __     __
            |_ _ _ _ __| |   _ _    \  |  |   |  |
                |  |     |  |    \   \ |  |   |  |
                |  |     |  |     |  | |  |_ _|  |     
                |  |     |  |     |  | |  |_ _|  | 
                |  |     |  |_ _ /  /  |  |   |  |
                |__|     |_ _ _ _ _/   |__|   |__|
            UI  Test  is  Starting      ...     ...     ...
                         """)
        # ------------------------ 处理一下获取到的参数----------------------------
        logger.debug(f"\n打印一下run方法的入参：{kwargs}\n")
        env_key = kwargs.get("env", "") or None
        marks = kwargs.get("m", "") or None

        # 如果命令行没有传递browser， 默认使用RunConfig.browser的值
        browser = kwargs.get("browser", "") or None
        RunConfig.browser = browser if browser else RunConfig.browser

        # 如果命令行没有传递mode， 默认使用RunConfig.mode的值
        mode = kwargs.get("mode", "") or None
        RunConfig.mode = mode.lower() if mode else RunConfig.mode
        # ------------------------ 捕获日志----------------------------
        # ------------------------ 设置pytest相关参数 ------------------------
        # arg_list = [f"--maxfail={RunConfig.max_fail}", f"--reruns={RunConfig.rerun}",
        #             f"--reruns-delay={RunConfig.reruns_delay}", f'--alluredir={ALLURE_RESULTS_DIR}',
        #             '--clean-alluredir']  # , "--screenshot=on"

        arg_list = [f"--maxfail={RunConfig.max_fail}", f'--alluredir={ALLURE_RESULTS_DIR}',
                    '--clean-alluredir']  # , "--screenshot=on"
        # if RunConfig.mode == "headed":
        #     arg_list.append("--headed")

        # if isinstance(RunConfig.browser, list):
        #     for browser in RunConfig.browser:
        #         arg_list.append(f"--browser={browser.lower()}")
        #         # arg_list.extend(["--browser", f"{browser.lower()}"])

        # if isinstance(RunConfig.browser, str):
        #     arg_list.append(f"--browser {RunConfig.browser.lower()}")

        if marks is not None:
            arg_list.append(f"-m {marks}")
            # arg_list.extend(["-m", f"{marks}"])
        # ------------------------ 设置全局变量 ------------------------
        # 根据指定的环境参数，将运行环境所需相关配置数据保存到GLOBAL_VARS
        ENV_VARS["common"]["env"] = ENV_VARS[env_key]["host"]
        GLOBAL_VARS.update(ENV_VARS["common"])
        GLOBAL_VARS.update(ENV_VARS[env_key])
        # ------------------------ pytest执行测试用例 ------------------------
        logger.debug(f"\n打印一下运行的参数：{arg_list}\n")
        pytest.main(args=arg_list)
        # ------------------------ 生成测试报告 ------------------------
        if kwargs.get("report") == "yes":
            report_path = generate_allure_report(allure_results=ALLURE_RESULTS_DIR,
                                                 allure_report=ALLURE_HTML_DIR,
                                                 windows_title=ENV_VARS["common"]["项目名称"],
                                                 report_name=ENV_VARS["common"]["报告标题"],
                                                 env_info={"运行环境": ENV_VARS["common"]["env"]},
                                                 allure_config_path=os.path.join(CONF_DIR,
                                                                                 "allure_config"), )
            # attachment_path=os.path.join(REPORT_DIR,
            #                              f'autotest_report.zip'))
            # ------------------------ 发送测试结果 ------------------------

            # send_result(report_info=ENV_VARS["common"], report_path=report_path, attachment_path=attachment_path)
    except Exception as e:
        raise e


if __name__ == '__main__':
    # 定义命令行参数
    parser = argparse.ArgumentParser(description="框架主入口")
    parser.add_argument("-env", default="test", help="输入运行环境：test 或 live")
    parser.add_argument("-m", default=None, help="选择需要运行的用例：python.ini配置的名称")
    parser.add_argument("-browser", nargs='*', help="浏览器驱动类型配置，支持如下类型：chromium, firefox, webkit")
    parser.add_argument("-mode", help="浏览器驱动类型配置，支持如下类型：headless, headed")
    parser.add_argument("-report", default="yes",
                        help="是否生成allure html report，支持如下类型：yes, no")
    args = parser.parse_args()
    run(**vars(args))
    server = HttpServer()
    server.run()
