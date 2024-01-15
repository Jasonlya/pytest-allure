# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/15 22:20
@Auth ： liangya
@File ：report_util.py
"""

import os

from XTestRunner import HTMLTestRunner
from config.config_path import reports_dir
from config.constants import r_filename, r_suite, r_title, r_blacklist, r_whitelist, r_description, r_tester


class ReportUtil:

    def set_report(self):
        filename = os.path.join(reports_dir, r_filename)
        # filename = 'reports/result.html'
        with open(filename, 'wb+') as f:
            # 注意这里要用wb的形式去写
            runner = HTMLTestRunner(stream=f,
                                    title=r_title,
                                    # blacklist=r_blacklist,
                                    # whitelist=r_whitelist,
                                    description=r_description,
                                    tester=r_tester,
                                    language="zh-CN")
            runner.run(r_suite)
            """
            blacklist是黑名单-->只有黑名单中的用例不会被执行
            whitelist是白名单-->只会执行白名单中的用例
            使用方法：
                @label("base")
                def test_01(self):
                    print("用例1")
            在用例上分添加@label("名字")，可以标记
            然后在HTMLTestRunner参数中添加@label标记的名字
            例如：
            blacklist=["名字"]
            """