#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.
# 创建chapter9的文件夹的快照（ZIP），命名格式为chapter9_1.zip、chapter9_2.zip

import zipfile,os
# 1.判断当前备份时第几个版本
# 2.现在备份该命名为哪个版本
# 3.添加压缩文件夹
def backupToZip(folder):
    os.chdir(folder)
    number = 1
    while True:
        BackupFileName = "chapter9_" + str(number) + ".zip"
        if not os.path.exists(BackupFileName):
            break
        number += 1

    print('Creating %s...' % (BackupFileName))
    BackupZip = zipfile.ZipFile(BackupFileName,'w')

    # 添加压缩文件
    # 遍历文件
    for folderName, subFolders, filenames in os.walk('.'):
        print('Adding files in %s... ' % folderName)

        for filename in filenames:
            if filename.endswith('.zip'):
                continue
            BackupZip.write(os.path.join(folderName,filename))
    
    BackupZip.close()
    print('Done!')




if __name__ == "__main__":
    backupToZip("D:\\Virtual\\PythonLearn\\chapter9")