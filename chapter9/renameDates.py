#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY
# 将带有美国风格日期的文件改名为欧洲风格日期
# 1.检查当前工作目录的所有文件名，寻找美国风格的日期
# 2.如果找到，将该文件改名，交换月份和日期的位置，使之成为欧洲风格。
# 这意味着代码需要做下面的事情：
# 1.创建一个正则表达式，可以识别美国风格日期的文本模式
# 2.调用os.listdir()，找出工作目录中的所有文件
# 3.循环遍历每个文件名，利用该正则表达式检查它是否包含日期
# 4.如果它包含日期，用shutil.move()对该文件改名

# 问题：正则表达式对于05-06-2021是5月6日还是6月5日呢？
# 我想我们都无法回答这个问题，别说正则表达式了
import shutil, os, re
# Create a regex that matches files with the American date format
datePattern = re.compile(r"""^(.*?)     # all text before the date
    ((0|1)?\d)-                         # one or two digits for the month
    ((0|1|2|3)?\d)-                     # one or two digits for the day
    ((19|20)\d\d)                       # four digits for the year
    (.*?)$                              # all text after the date
    """, re.VERBOSE)
# datePattern = re.compile(r"""^(1)   # all text before the date
#     (2(3))-                         # one or two digits for the month
#     (4(5))-                         # one or two digits for the day
#     (6(7))                          # four digits for the year
#     (8)$                            # all text after the date
# """, re.VERBOSE)

# Loop over the files in the working directory.
os.chdir('D:\\Virtual\\PythonLearn\\chapter9')
for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)

    # skip files without a date.
    if mo == None:
        continue
    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    # Form the European-style filename
    euroFileName = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart
    # Get the full,absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    #Rename the files
    print('Renaming "%s" to "%s"...' % (amerFileName,euroFileName))
    shutil.move(amerFileName,euroFileName)



