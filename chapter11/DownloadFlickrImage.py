#! python3
# 下载filckr.com网站的图片搜索的图片

# 0.打开网站使用requests模块get请求
# 2.通过处理返回包获取图片的URL
# 3.批量化写入图片文件



text = "美女"

import os
os.environ["http_proxy"] = "http://127.0.0.1:33210"
os.environ["https_proxy"] = "http://127.0.0.1:33210"
url = "https://www.flickr.com/search/?text=" + text

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

browser = webdriver.Firefox()
browser.get(url)
time.sleep(1)

# pictureElems = browser.find_elements(By.CLASS_NAME,"overlay")
# i = 0
# for pictureElem in pictureElems:
#     print(pictureElem.get_attribute('href') + " 正在下载中...")
#     imageFile = open('D:\\Virtual\\PythonLearn\\chapter11\\image\\' + str(i) + '.jpg', 'wb')
#     res = requests.get(pictureElem.get_attribute('href'))
#     for item in res.iter_content(10000):
#         imageFile.write(item)
#     print(pictureElem.get_attribute('href') + " 下载完成")
#     i +=1

