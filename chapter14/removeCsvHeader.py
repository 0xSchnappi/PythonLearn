#! python3
# removeCsvHeader.py - 要删除几百CSV文件的第一行


from fileinput import filename
from genericpath import exists
import os, csv

os.chdir("D:\\Virtual\\PythonLearn\\chapter14")
os.makedirs("headerRemoved", exist_ok=True)

for fileName in os.listdir('.'):
    csvRows = []
    if fileName.endswith('.csv'):
        print(fileName)

        # 读csv文件
        csvFile = open(fileName)
        readerObj = csv.reader(csvFile)
        for row in readerObj:
            if readerObj.line_num == 1:
                continue
            csvRows.append(row)
        csvFile.close()

        # 写入csv文件
        csvFileObj = open(os.path.join('headerRemoved', fileName), 'w', newline='')
        csvWriter = csv.writer(csvFileObj)
        for row in csvRows:
            csvWriter.writerow(row)
        csvFileObj.close()