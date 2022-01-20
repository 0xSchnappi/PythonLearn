#! python3
# 选择性拷贝
# 编写一个程序，遍历一个目录树，查找特定扩展名文件（诸如.pdf或.jpg）
# 不论这些文件的位置在哪里，将他们拷贝到一个新的文件夹中
from ctypes.wintypes import INT
from fileinput import filename
import os,shutil,re

def FindFile(folder):
    print("查找 '%s' 文件夹pdf文件")
    for folderName, subfolders, filenames in os.walk(folder):
        for fileName in filenames:
            if fileName.endswith('.pdf'):
                print(os.path.join(folder,fileName))
                fileName = os.path.join(folder,fileName)
                shutil.copy(fileName,"E:\\OneDrive\\桌面\\blog\\PDF")
                
        

# 删除不需要的文件
# 一些不需要的、巨大的文件或文件夹占据了硬盘的空间，这并不少见。如果你
# 试图释放计算机上的空间，那么删除不想要的巨大文件效果最好。但首先你必须找到它们
# 编写一个程序，遍历一个目录树，查找特别大的文件或文件夹，比方说，超过
# 100MB的文件(回忆一下，要获取文件的大小，可以使用os模块的os.path.getsize())。
# 将这些文件的绝对路径打印到屏幕上
def FindBigFile():
    folder = "D:\\"
    for folderName, subfolders, filenames in os.walk(folder):
        for fileName in filenames:
            fileName = os.path.join(folderName,fileName)
            if os.path.getsize(fileName) > 1024*1024*1024:  #1GB=1024*1024*1024
                print(fileName)

# 消除缺失的编号
# 编写一个程序，在一个文件夹中，找到所有带指定前缀的文件，诸如spam001.txt，spam002.txt等，
# 并定位缺失的编号（例如存在spam001.txt和spam003.txt，但不存在spam002.txt）。让该程序对所有后面的文件改名，消除缺失的编号
# 作为附加的挑战，编写另一个程序，在一些连续的编号的文件中，空出一些编号，以便加入新的文件
# 1.遍历文件夹中的文件名
# 2.正则表达式匹配


def spamDeleteNumber(folder):
    startNumber = 1
    NumberRegex = re.compile(r'spam(\d\d\d)\.txt')
    for folderName, subFloderName, fileNames in os.walk(folder):
        for fileName in fileNames:
            mo = NumberRegex.search(fileName)
            if mo != None:
                if startNumber < 10:
                    fileRename = "spam" + str(startNumber).rjust(3, '0') + ".txt"
                elif startNumber < 100:
                    fileRename = "spam" + str(startNumber).rjust(2, '0') + ".txt"
                else:
                    fileRename = "spam" + str(startNumber) + ".txt"
                startNumber += 1
                print(fileName + " Rename to :%s" % (fileRename))
                shutil.move(os.path.join(folderName,fileName), os.path.join(folderName,fileRename))
   
def spamAddNumber(folder):
    startNumber = 1
    NumberRegex = re.compile(r'spam(\d\d\d)\.txt')
    for folderName, subFloderName, fileNames in os.walk(folder):
        for fileName in fileNames:
            mo = NumberRegex.search(fileName)
            if mo != None:
                if startNumber < 10:
                    fileRename = "spam" + str(startNumber).rjust(3, '0') + ".txt"
                elif startNumber < 100:
                    fileRename = "spam" + str(startNumber).rjust(3, '0') + ".txt"
                else:
                    fileRename = "spam" + str(startNumber).rjust(3, '0') + ".txt"
                startNumber += 100        # 空100个编号
                print(fileName + " Rename to :%s" % (fileRename))
                shutil.move(os.path.join(folderName,fileName), os.path.join(folderName,fileRename))

if __name__ == "__main__":
    FindFile("E:\\OneDrive\\桌面\\blog")
    FindBigFile()
    spamDeleteNumber("D:\\Virtual\\PythonLearn\\chapter9")
    spamAddNumber("D:\\Virtual\\PythonLearn\\chapter9")