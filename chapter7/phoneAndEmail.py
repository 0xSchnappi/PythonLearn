# 代码流程
# 1.从剪贴板取得文本
# 2.找出文本中所有的电话号码和E-mail地址
# 3.将他们粘贴到剪贴板
# 实现：
# 1.使用pyperclip模块复制和粘贴字符串
# 2.创建两个正则表达式，一个匹配电话号码、另一个匹配E-mail地址
# 3.对两个正则表达式找到所有匹配，而不只是第一次匹配
# 4.将匹配的字符串整理好格式，放在一个字符串中，用于粘贴
# 5.如果文本中没有找到匹配，显示某种消息


#! python3
# phoneAndEmail.py
import pyperclip,re

# 第一步：为电话号码创建一个正则表达式
phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?              # areas code
                        (\s|-|\.)?                      # separator
                        (\d{3})                           # first 3 digits
                        (\s|-|\.)                       # separator
                        (\d{4})                           # last 4 digits
                        (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
                        )''',re.VERBOSE)

# 第二步：为E-mail地址创建一个正则表达式
emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+       # uername
                        @
                        [a-zA-Z0-9.-]+          # domain name
                        (\.[a-zA-Z]{2,4})
                        )''',re.VERBOSE)

# 第三步：在剪贴板文本中找到所有匹配
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[0] != '':
        phoneNum += ' X' + groups[0]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# 第四步：所有匹配连接成一个字符串，复制到剪贴板
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or emai address found')