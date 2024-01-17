import os

base_dir = os.path.dirname(os.path.dirname(__file__))

# 驱动地址 无法放入项目中读取，只能手动指定驱动位置
# driver_path = os.path.abspath("D:/driver/chromedriver73.exe")

# # 测试用例路径
# cases_dir = os.path.join(base_dir, 'testcases')

# 测试数据路径
yaml_datas_dir = os.path.join(base_dir, 'datas', 'yaml_data')
xls_datas_dir = os.path.join(base_dir, 'datas', 'xls_data')
csv_datas_dir = os.path.join(base_dir, 'datas', 'csv_data')

# 配置模块目录
CONF_DIR = os.path.join(base_dir, "config")

# 日志路径
logs_dir = os.path.join(base_dir, 'outputs', 'logs')

# 日志/报告保存目录
OUT_DIR = os.path.join(base_dir, "outputs")
if not os.path.exists(OUT_DIR):
    os.mkdir(OUT_DIR)

# 报告保存目录
REPORT_DIR = os.path.join(OUT_DIR, "report")
if not os.path.exists(REPORT_DIR):
    os.mkdir(REPORT_DIR)

# 截图路径
screenshots_dir = os.path.join(base_dir, 'outputs', 'screenshots')

# 第三方库目录
LIB_DIR = os.path.join(base_dir, "lib")

# Allure报告，测试结果集目录
ALLURE_RESULTS_DIR = os.path.join(REPORT_DIR, "allure_results")

# Allure报告，HTML测试报告目录
ALLURE_HTML_DIR = os.path.join(REPORT_DIR, "allure_html")
