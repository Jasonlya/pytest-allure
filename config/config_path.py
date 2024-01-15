import os

base_dir = os.path.dirname(os.path.dirname(__file__))


# 测试用例路径
cases_dir = os.path.join(base_dir, 'testcases')

# 测试数据路径
yaml_datas_dir = os.path.join(base_dir, 'datas', 'yaml_data')
xls_datas_dir = os.path.join(base_dir, 'datas', 'xls_data')
csv_datas_dir = os.path.join(base_dir, 'datas', 'csv_data')
# 日志路径
logs_dir = os.path.join(base_dir, 'outputs', 'logs')

# 报告路径
reports_dir = os.path.join(base_dir, 'outputs', 'reports')

# 截图路径
screenshots_dir = os.path.join(base_dir, 'outputs', 'screenshots')

