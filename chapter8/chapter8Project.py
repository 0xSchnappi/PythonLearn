#!python3
# chaper8Project.py
# Project2:疯狂填词
# 创建一个疯狂填词程序，它将读入文本文件，并让用户在该文本文件中
# 出现ADJECTIVE、NOUN、ADVERB或VERB等单词的地方，加上他们自己的文本。
# 例如，一个文本文件可能看起来像这样：
# 1.打开文件
# 2.正则匹配ADJECTIVE、NOUN、ADVERB或VERB等单词
# 3.修改字符串
# 4.覆写模式写文件


from asyncore import read
from ctypes.wintypes import WORD
from os import path
import re
from tokenize import group
madLibsFile = open('D:\\Virtual\\PythonLearn\\chapter8\\MadLibs.txt')
contents = madLibsFile.read()
print(contents)

wordRegex = re.compile('ADJECTIVE|NOUN|ADVERB|VERB')
while 1:
    if wordRegex.search(contents):
        item = wordRegex.search(contents).group().lower()
        if item[0].lower() == 'a' or item[0].lower() == 'o' or item[0].lower() == 'e' or item[0].lower() == 'i' or item[0].lower() == 'u' or item[0].lower() == 'v':
            print('Enter an %s' % item)
        else:
            print('Enter a %s' % item)
        word = input()
        contents = wordRegex.sub(word, contents, count = 1)
    else:
        break;

# Project3:正则表达式
# 编写一个程序，打开文件夹中所有的.txt文件，查找匹配用户提供的正则表达式的所有行。结果应该打印到屏幕上。
import os,re
path = "D:\\Virtual\\PythonLearn\\chapter8"
Regex = "Hello World"
wordRegex = re.compile('%s' % Regex)

for filename in os.listdir(path):
    if filename[-3:].lower() == 'txt':
        fp = open(os.path.join(path,filename))
        for item in fp.readlines():
            if wordRegex.search(item) != None:
                print(filename)
                print(item)
        fp.close()
        
