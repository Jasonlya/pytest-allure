# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/8 0:56
@Auth ： liangya
"""
import os

import yaml, csv, pandas as pd
# import xlrd
from config.config_path import yaml_datas_dir, csv_datas_dir, xls_datas_dir


class DataUtil:

    # 读取yaml文件
    def read_yaml(self, yaml_name):
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'datas', yaml_name)
        with open(file_path, 'r+', encoding='utf-8') as file:
            data = yaml.load(stream=file, Loader=yaml.FullLoader)
            return data

    # 读取csv文件，返回是元组（需要用 * 解除元祖）
    def read_csv_tuple(self, filename):
        """ filename文件名 """
        filepath = os.path.join(csv_datas_dir, filename)
        with open(filepath, encoding='utf-8') as file:
            data_list = csv.reader(file)
            i = 1
            list_data = []
            for row in data_list:
                if i > 1:
                    list_data.append(row)
                i = i + 1
            # print(tuple(list_data))
            return tuple(list_data)

    # 读取excel文件（xlsx或xls）
    def read_xlsx_tuple(self, filename, sheet_name='Sheet1'):
        """ filename文件名 sheet_name表单名"""
        filepath = os.path.join(xls_datas_dir, filename)
        df = pd.read_excel(filepath, sheet_name=sheet_name)
        return tuple(df.values)


if __name__ == '__main__':
    data = DataUtil().read_yaml('../datas/add_permission.yml')
    print(tuple(data))
