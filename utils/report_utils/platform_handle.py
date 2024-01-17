
# 标准库导入
import os.path
import platform
# 本地应用/模块导入
from config.config_path import LIB_DIR


class PlatformHandle:
    """跨平台的支持allure, webdriver"""

    @property
    def allure(self):
        allure_bin = os.path.join(LIB_DIR, [i for i in os.listdir(LIB_DIR) if i.startswith("allure")][0], "bin")
        if platform.system() == "Windows":
            allure_path = os.path.join(allure_bin, "allure.bat")
        else:
            allure_path = os.path.join(allure_bin, "allure")
            os.popen(f"chmod +x {allure_path}").read()
        return allure_path


if __name__ == '__main__':
    res = PlatformHandle().allure
    print(res)
