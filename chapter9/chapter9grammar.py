# shutil模块的一些函数包括移动、改名和删除文件
import shutil, os
# 用于复制文件和整个文件夹
# shutil.copy(source,destination)，将路径source处的文件复制到路径destination处的文件夹。
# 如果destination是一个文件名，它将作为被复制文件的新名字。该函数返回一个字符串，表示复制文件的路径。
# print(shutil.copy('D:\\Virtual\\PythonLearn\\chapter8\\bacon.txt', 'D:\\Virtual\\PythonLearn\\chapter9'))
# print(shutil.copy('D:\\Virtual\\PythonLearn\\chapter9\\bacon.txt','D:\\Virtual\\PythonLearn\\chapter9\\ba.txt'))

# shutil.copytree(source, destination)，将路径source处的文件夹，包含它的所有文件和子文件夹，复制到destination处的文件夹
# destination是新创建的文件夹
# print(shutil.copytree('D:\\Virtual\\PythonLearn\\chapter1','D:\\Virtual\\PythonLearn\\chapter1_backup'))

# 文件和文件夹的移动与改名
# shutil.move(source, destination),将路径source处的文件夹移动到路径destination，并返回绝对路径的字符串
# print(shutil.move('D:\\Virtual\\PythonLearn\\chapter9\\ba.txt', 'D:\\Virtual\\PythonLearn\\chapter1_backup'))
# 假定chapter9目录下没有ba_backup文件夹，ba.txt就会改名为ba_backup
# print(shutil.move('D:\\Virtual\\PythonLearn\\chapter1_backup\\ba.txt', 'D:\\Virtual\\PythonLearn\\chapter9\\ba_backup'))

# 永久删除文件和文件夹
# 利用os模块中的函数，可以删除一个文件或一个空文件夹，但利用shutil模块，可以删除一个文件夹及其所有的内容
# 用os.unlink(path)将删除path处的文件
# 调用os.rmdir(path)将删除path处的文件夹。该文件夹必须为空，其中没有任何文件和文件夹
# 调用shutil.rmtree(path)将删除path处的文件夹，它包含的所有文件和文件夹都会被删除
for filename in os.listdir('D:\\Virtual\\PythonLearn\\chapter9'):
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)

# 用send2trash模块安全地删除
import send2trash
# shutil.rmtree(path)不可恢复的删除文件和文件夹
# send2trash会将文件发送到计算机的垃圾箱或回收站，而不是永久删除它们
# send2trash.send2trash('D:\\Virtual\\PythonLearn\\chapter9\\ba_backup')

# 遍历目录树
# 假定你希望对某个文件夹中的所有文件改名，包括该文件夹中所有子文件夹中的所有文件
# os.walk()返回字符串的列表
for folderName, subfolders, filenames in os.walk('D:\\Virtual\\PythonLearn'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ": " + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')

# 用zipfile模块压缩文件
import zipfile
os.chdir('D:\\Virtual\\PythonLearn\\chapter9')
exampleZip = zipfile.ZipFile('PythonLearn-master.zip')
print(exampleZip.namelist())
mydataInfo = exampleZip.getinfo('PythonLearn-master/chapter8/mydata.dat')
print(mydataInfo.file_size)
print(mydataInfo.compress_size) # 压缩后问价大小
print('Compressed file is %sx smaller!' % (round(mydataInfo.file_size / mydataInfo.compress_size, 2)))
# 解压
print(exampleZip.extractall())
print(exampleZip.extract('PythonLearn-master/chapter8/mydata.dat','new\\folders'))
# 创建和添加到zip文件
newZip = zipfile.ZipFile('new.zip','w')
print(newZip.write('new\\folders\\PythonLearn-master\\chapter8\\mydat.dat', compress_type=zipfile.ZIP_DEFLATED))
exampleZip.close()