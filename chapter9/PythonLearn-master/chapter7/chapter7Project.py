#!python3
# chapter7Project.py
# project1:强口令检测
# 写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。
# 强口令的定义是：长度不少于8个字符，同时包含大写和小写字符，
# 至少有一位数字，你可能需要用多个正则表达式来测试该字符串，以保证它的强度
from pickle import FALSE, TRUE
import re
from unittest import result

def StrongPasswordDetection(password):
    passwordLengthRegex = re.compile(r'(.){8,}')
    passwordUpperRegex = re.compile(r'[A-Z]')
    passwordLowerRegex = re.compile(r'[a-z]')
    passwordDecimalRegex = re.compile(r'[0-9]')

    bOk = False

    if passwordLengthRegex.search(password) != None:   
        if passwordUpperRegex.search(password) != None:           
            if passwordLowerRegex.search(password) != None:              
                if passwordDecimalRegex.search(password) != None:
                    bOk = TRUE
                else:
                    print(password + " 密码至少一位数字!")
            else:
                print(password + " 密码缺少小写字母!")
        else:
            print(password + " 密码缺少大写字母!")
    else:
        print(password + " 密码长度至少8位!")


    if bOk:
        print(password + " is strong password!")
    else:
        print(password + " is weak password!")



# project2:strip()的正则表达式版本
# 写一个函数，他接受一个字符串，做的事情和strip()字符串方法一样。
# 如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。
# 否则，函数第二个参数指定的字符，将从该字符串中去除。

def RewriteStrip(text, Str = ' '):
    textStrip = ''
    if Str == ' ':
        headSpaceRegex  = re.compile(r'^\s*')
        headTextStrip = headSpaceRegex.sub(r'',text)
        tailSpaceRegex = re.compile(r'(\s*)$')
        textStrip = tailSpaceRegex.sub(r'',headTextStrip)
    else:
        strRegex = re.compile(r"(%s)"%Str)
        if strRegex.search(text) != None:
            textStrip = strRegex.sub(r'',text)
        else:
            print("字符串'" + text + "'中没有'" + Str + "'字符")
            return None     
    return textStrip
    



# 测试
if __name__ == "__main__":
    StrongPasswordDetection("Aa11111111111111")
    print(RewriteStrip('   hdshfhs  ','1'))
    print(RewriteStrip('   hdshfhs  '))
    print(RewriteStrip('   hdshfhs  ','d'))