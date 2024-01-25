# pytest-allure
   本文为搭建python-selenium-pytest-allure-log UI自动化测试框架

## 1.安装配置
- ### python安装

- ### jdk安装
      自行安装。公司jdk1.8.0_202即可

- ### allure安装

      解压安装包
      设置环境变量
      查看是否安装成功
- ### python相关模块安装
```      
      设置python三方模块下载源

      下载源地址设置：pip config set global.index-url 'http://192.168.13.126:8000'

      设置信任此地址：pip config set global.trusted-host '192.168.13.126'
```
## 2.目录解释
```
│  pytest.ini           ##pytest框架配置
│  QUESTION.md          ##问题收集
│  README.md            ##说明文档
│  run.py               ##执行入口
│          
├─common                ##用于公共的操作方法、全局变量定义
│  │   base_page.py     ##页面操作基础方法
│  │   global_var.py    ##全局变量
│      
├─config                ##公共配置
│  │  conf.py           ##公共配置
│  │  config_path.py    ##路径配置
│          
├─datas                 ##数据目录
│      test_input.xlsx
│      
├─outputs               ##输出目录，包括报告、日志、截图
│  └─allure             
│              
├─page_locations        ##page层，用于存放各页面元素定位
│      
│      
├─page_objects          ##页面对象，用于存放页面相关方法
│      
│      
├─testcases             ##测试用例目录
│      
│      conftest.py      ##夹具存放目录
│      
├─util                  ##工具类目录

```
## 3.运行路径

## 4.测试用例编写

## 5.参考文档
geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases

Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html

operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver