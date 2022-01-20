# Project:口令保管箱
# 第一步：程序设计和数据结构
# 第二步：处理命令行参数
# 第三步：复制正确的口令

#! python3
# pw.py - An insecure password locker program.
PASSWORDS = {'email':'E-mailPassword',
            'blog':'0xSchnappi',
            'luggage':'12345'}

import sys,pyperclip
if len(sys.argv) < 2:
    print('Usage: python3 pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
if account == '-h' or account == '--help':
    print('Usage: python3 pw.py [account] - copy account password')
    sys.exit()
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)