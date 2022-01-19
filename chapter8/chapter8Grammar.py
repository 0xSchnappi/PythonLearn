# 读写文章
# Windows上的倒斜杠以及OS X和Linux上的正斜杠
from fileinput import close
import os
from posixpath import dirname
print(os.path.join('usr','bin','spam'))

myFile = ['accounts.txt','details.csv','invite.docx']
for filename in myFile:
    print(os.path.join('D:\Virtual\PythonLearn\chapter8',filename))

# 当前工作目录
print(os.getcwd())
# 将当前工作目录改为C:\Windows\System32
#os.chdir('C:\Windows\System32')
print(os.getcwd())
# 创建文件夹
#os.makedirs('D:\Virtual\PythonLearn\chapter8\waffles')

# 处理绝对路径和相对路径
# 将相对路径转换位绝对路径
print(os.path.abspath('.'))
# 检查是否为绝对路径
print(os.path.isabs('D:\Virtual\PythonLearn'))
print(os.path.isabs('.'))
# relpath(path,start)将返回从start路径到path的相对路径的字符串
print(os.path.relpath('D:\\','D:\\Virtual\\PythonLearn\\chapter8'))
print(os.path.relpath('D:\\Virtual\\PythonLearn\\chapter8','D:\\'))

path = 'C:\Windows\System32\calc.exe'
print(os.path.dirname(path))
print(os.path.basename(path))

# 查看文件大小和文件夹内容
print(os.path.getsize(path))
# print(os.listdir(os.path.dirname(path)))

# totalSize = 0
# for filename in os.listdir(os.path.dirname(path)):
#     totalSize = totalSize + os.path.getsize(os.path.join('C:\Windows\System32',filename))
# print(totalSize)

# 检查路径有效性
# os.path.exists(path) 检查文件或文件夹
# os.path.isfile(path) 检查一个文件
# os.path.isdir(path) 检查一个文件夹
print(os.path.exists('C:\Windows\System32'))
print(os.path.exists('C:\Windows\System32\calc.exe'))

print(os.path.isfile('C:\Windows\System32'))
print(os.path.isfile('C:\Windows\System32\calc.exe'))

print(os.path.isdir('C:\Windows\System32'))
print(os.path.isdir('C:\Windows\System32\calc.exe'))

# 文件读写过程
# 1.调用open()函数，返回一个File对象
# 2.调用File对象的read()或write()方法
# 3.调用File对象的close()方法，关闭该文件
helloFile = open('D:\Virtual\PythonLearn\chapter8\hello.txt')
helloContent = helloFile.read()
print(helloContent)
helloFile.close()
# 返回列表
# helloFile = open('D:\Virtual\PythonLearn\chapter8\hello.txt')
helloFile = open('D:\Virtual\PythonLearn\chapter8\hello.txt','r')
helloList = helloFile.readlines()
print(helloList)

# 写模式：'w' 覆写原有文件，从头开始，就像你用一个新值覆写一个变量的值
# 添加模式：'a' 在已有文本末尾添加文本
baconFile = open('.\\chapter8\\bacon.txt','w')
baconFile.write('Hello World\n')
baconFile.close()

baconFile = open('D:\\Virtual\\PythonLearn\\chapter8\\bacon.txt','a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('D:\\Virtual\\PythonLearn\\chapter8\\bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

# 用shelve模块保存变量
import shelve
shelfFile = shelve.open('D:\\Virtual\\PythonLearn\\chapter8\\mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('D:\\Virtual\\PythonLearn\\chapter8\\mydata')
print(type(shelfFile))
print(shelfFile['cats'])
# 就像列表一样有keys()和values()方法
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

# 用pprint.pformat()函数保存变量
import pprint
# pprint.pprint() 漂亮打印
# pprint.pformat() 返回既易于阅读又符合python语法
cats = [{'name':'Zophie', 'desc':'chubby'},{'name':'Pooka', 'desc':'fluffy'}]
print(pprint.pformat(cats))

# fileObj = open('D:\\Virtual\\PythonLearn\\chapter8\\myCats.py','w')
# fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
# fileObj.close()

import myCats
print(myCats.cats)
print(myCats.cats[1])
print(myCats.cats[1]['name'])