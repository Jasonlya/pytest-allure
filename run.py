# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:44
@Auth ： liangya
@File ：run.py
"""
import pytest
import os

#if __name__ == '__main__':
    #pytest.main(['-v', '-s',  '--alluredir', 'report/''TestCases/'])

if __name__ == '__main__':
    pytest.main(['-s', '-q','./','--clean-alluredir','--alluredir=report'])
    #os.system('cp environment.properties ./allure-results/environment.properties')
    os.system("allure generate -c -o allure-report")