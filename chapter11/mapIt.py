#! python3
# 将一条街道的地址拷贝到剪贴板，并在Google地图上打开它的地图。
# 写一个简单的脚本，利用剪贴板中的内容在浏览器中自动加载地图。这样，
# 你只要将地址拷贝到剪贴板，运行该脚本，地图就会加载
# 1.从命令行参数或剪贴板中获取街道地址
# 2.打开Web浏览器，指向该地址的Google地图页面
# 这意味代码需要做下列事情
# 1.从sys.argv读取命令行参数。
# 2.读取剪贴板内容。
# 3.调用webbrowser.open()函数打开外部浏览器
import webbrowser, sys, pyperclip, re
# webbrowser.open('https://baidu.com')    # 使用电脑的默认浏览器打开https://baidu.com
# 在Googel map中查找王府井街道 对URL并进行分析
# https://www.google.com/maps/place/Wang+Fu+Jing+Da+Jie,+Dong+Cheng+Qu,+Bei+Jing+Shi,+China,+100006/@39.9112741,116.4091913,17z/data=!3m1!4b1!4m5!3m4!1s0x35f052d1d66b73b9:0xd212cf432caac4d6!8m2!3d39.91127!4d116.41138
# 
if len(sys.argv) > 1:
    # Get address from command line.
    # PS D:\Virtual\PythonLearn> & C:/Python39/python.exe D:\Virtual\PythonLearn\chapter11\mapIt.py WangFuJingDaJie
    address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard.
else:
    # Get address from clipboard.
    # 复制WangFuJingDaJie运行
    address = pyperclip.paste()
addressRegex = re.compile(r'[A-Z]{1}[a-z]*')
googleAddress = ''
for item in addressRegex.findall(address):
    googleAddress += item + '+'
webbrowser.open('https://www.google.com/maps/place/' + googleAddress[:-1])
