# 字符串操作
# 引号使用
# 利用双引号
spam = "That is Alice's cat."
print(spam)
# 利用转义字符
spam = 'Say hi to Bob\'s mother'
print(spam)
# 原始字符串
print(r'That is Carol\'s cat.')
# 三重引号的多行字符串
# 单引号不需要转义
print('''Dear Alice
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely
Bob''')
# 多行注释
"""
注释1
"""
'''
注释2
'''
# 字符串下标和切片
spam = "Hello World"
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])
# 字符串的in和not in操作
print('Hello' in 'Hello World')
print('Hello' in 'Hello')
print('HELLO' in 'Hello world')
print('' in 'spam')
print('cats' not in 'cats and dogs')
# 字符串方法upper()、lower()、isupper()和islower()
spam = "Hello World"
print(spam.upper())
print(spam.lower())
print(spam.isupper())
print('HELLO'.isupper())
print(spam.islower())
print('hello'.islower())
# isX字符串方法
# isalpha()如果字符串只包含字母，并且非空，返回true；
# isalnum()如果字符串只包含字母和数字，并且非空，返回true；
# isdecimal()如果字符串只包含数字字符，并且非空，返回true；
# isspace()如果字符串只包含空格、制表符和换行，并且非空，返回true
# istitle()如果字符串仅包含以大写字母开头、后面都是小写字母的单词
#
# 字符串方法startswitch()和endswitch()
print('Hello World'.startswith('Hello'))
print('Hello World'.endswith('World'))
print('Hello World'.startswith('H123'))
# 字符串方法join()和split()
# 连接字符串列表
print(','.join(['cats','rats','bats']))
print(' and '.join(['cats','rats','bats']))
# split()正好相反
print('My name is Simon'.split())
print('cats and rats and bats'.split(' and '))
# 用rjust()、ljust()和center()方法对齐文本
print('Hello'.rjust(10))
print('Hello'.ljust(10))
print('Hello'.center(20,'='))
# 用strip()、rstrip()和lstrip()删除空白字符
spam = ' Hello World '
print(spam.rstrip())
print(spam.lstrip())
print(spam.strip())
# 用pyperclip模块拷贝粘贴字符串
import pyperclip
pyperclip.copy('Hello World')
print(pyperclip.paste())

