#!python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:    py.exe mcb.pyw save <keyword> - Save clipboard to keyword
#           py.exe mcb.pyw <keyword> - loads keyword to clipboard
#           py.exe mcb.pyw list - Loads all keywords to clipboard
#           py.exe mcb.pyw delete <keyword> - delete keyword to text
# 多重剪贴板
# mcb.pyw multiclipboard    .pyw扩展名意味着python运行该程序时，不会显示终端窗口
# 该程序将利用一个关键字保存每段剪切板文本。例如，当运行py mcb.pyw save spam，
# 剪贴板中当前的内容就用关键字spam保存。通过运行py mcb.pyw spam，这段文本稍后将重新加载到剪贴板中。
# 如果用户忘记了都有哪些关键字，他们可以运行py mcb.pyw list，将所有关键字的列表复制到剪贴板中。
# 下面是程序要做的事
# 1.针对要检查的关键字，提供命令行参数。
# 2.如果参数是save，那么将剪贴板的内容保存到关键字
# 3.如果参数是list，就将所有的关键字拷贝到剪贴板
# 4.否则，就将关键词对应的文本拷贝到剪贴板
# 这意味着代码需要做下列事情
# 1.从sys.argv读取命令行参数
# 2.读取剪贴板
# 3.保存并加载shelf文件
# 如果你是要Windows，可以创建一个名为mcb.bat的批处理文件，很容易地同“Run……”窗口运行这个脚本。
# 该批处理文件包含如下内容：
# @pyw.exe D:\Virtual\PythonLearn\chapter8\mcb.pyw %*

import shelve, pyperclip, sys

mcbShelf = shelve.open('D:\\Virtual\\PythonLearn\\chapter8\\mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('clipboard is :\'' + str(list(mcbShelf.keys())) + '\'')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print('clipboard is :\'' + mcbShelf[sys.argv[1]] + '\'')

mcbShelf.close()


