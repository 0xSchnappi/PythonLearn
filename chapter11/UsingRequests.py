#! python3
# 使用Requests模块

import requests

res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))

if res.status_code == requests.codes.ok:
    # requests.codes.ok 200
    print(len(res.text))
    print(res.text[:250])


res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()      # 确保程序在下载失败时停止
except Exception as exc:
    print('The was a problem: %s' % exc)

# 将下载的文件保存到硬盘
# 首先必须用“写二进制”模式打开该文件，即向函数传入字符串'wb'，作为open()的第二个参数。
# 即使该页面时纯文本的，你也需要写入二进制数据，而不是文本数据，目的是为了保存该文本的“Unicode编码”
res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')
if res.status_code == requests.codes.ok:
    playFile = open('d:\\Virtual\\PythonLearn\\chapter11\\RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):  # 循环读写一万字节
        playFile.write(chunk)
    playFile.close()

