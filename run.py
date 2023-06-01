# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/30 22:44
@Auth ： liangya
@File ：run.py
"""
import pytest
import os

# if __name__ == '__main__':
#     pytest.main(['-v', '-s',  '--alluredir', 'allure-report/''TestCases/'])

if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./temp/html -o ./report  --clean")
    # os.system('cp environment.properties.properties ./allure-results/environment.properties')
    # os.system("allure generate -c -o allure-report")
    # pytest.main()