# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/7 22:31
@Auth ： liangya
"""

import pytesseract
from PIL import Image

def operationyzm(image):
    # 读取验证码图片
    image = Image.open(image)

    # 将图片转化为灰度图像
    image = image.convert('L')

    # 对图像进行二值化处理
    threshold = 127
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')

    # 调用 pytesseract 进行识别
    code = pytesseract.image_to_string(image)
    print(code)
    return code

if __name__ == '__main__':
    # image=r'F:\PycharmProjects\pytest-allure\pytest-allure\page_locations\PageObject_YWPT\yzm.png'
    # E:\project\pytest - allure\img.png  E:\project\pytest-allure\page_locations\PageObject_YWPT\yzm.png
    operationyzm(r'F:\PycharmProjects\pytest-allure\pytest-allure\util\TEST2.png')