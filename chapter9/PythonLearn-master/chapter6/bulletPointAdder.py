#! python3
# bulletPointAdder.py - Add Wikipedia bullet points to the start
# of each line of text on the clipboard
# 第一步：从剪贴板中复制和粘贴
# 第二步：分离文本中的行，并添加星号
# 第三步：连接修改过的行
# example:

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n') # 删除\r\n后得到一个字符串列表
print(lines)
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
print(lines)
# 连接字符串列表
text = '\n'.join(lines)
print(text)
pyperclip.copy(text)