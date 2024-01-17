# -*- coding: utf-8 -*-
# @Time    : 2023/5/24 9:34
# @Author  : chenyinhua
# @File    : http_server.py
# @Software: PyCharm
# @Desc: 封装的HTTP服务

# 标准库导入
import http.server
import socketserver
import os
import sys
# 第三方库导入
from functools import partial
from config.config_path import ALLURE_HTML_DIR


class HttpServer:
    def __init__(self, bind: str = "127.0.0.1", port: int = 8000, directory=ALLURE_HTML_DIR):
        """
        :param bind: 指定地址，如本地主机
        :param port: 自定义端口号, 服务器默认监听端口是 8000
        :param directory: 指定工作目录, 服务器默认工作目录为当前目录
        """
        self.bind = bind
        self.port = port
        self.directory = directory
        args = sys.argv
        for i in range(1, len(args)):
            if args[i] == "-port" and i + 1 < len(args):
                self.port = int(args[i + 1])
            if args[i] == "-dir" and i + 1 < len(args):
                self.directory = args[i + 1]
            if args[i] == "-bind" and i + 1 < len(args):
                self.bind = args[i + 1]

    def run(self):
        try:
            with socketserver.TCPServer((self.bind, self.port), partial(http.server.SimpleHTTPRequestHandler,
                                                                        directory=self.directory)) as httpd:
                print(
                    f"报告路径：{self.directory}\n"
                    f"Serving HTTP on {self.bind} port {self.port} \n"
                    f"打开查看报告：http://{self.bind}:{self.port}/ ..."
                )
                httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            sys.exit(0)


if __name__ == '__main__':
    server = HttpServer()
    server.run()
