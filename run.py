# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:44
@Auth ： liangya
@File ：run.py
"""
import pytest
import os
from  util.operationpath import get_path

# if __name__ == '__main__':
#     pytest.main(['-v', '-s',  '--alluredir', 'allure-report/''TestCases/'])

if __name__ == '__main__':
    pytest.main(['-v','-s','-k' 'test_loginywpt'])
    # os.system("allure generate ./temp/html -o ./report  --clean")
    # os.system(f"allure serve .report/temp -h 127.0.0.1 -p 9999")
    # os.system('cp environment.properties.properties ./allure-results/environment.properties')
    # os.system("allure generate -c -o allure-report")
    # pytest.main()