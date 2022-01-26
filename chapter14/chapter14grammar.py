#! python3
# chapter14grammar.py
# CSV模块
import csv
exampleFile = open('D:\\Virtual\\PythonLearn\\chapter14\\example.csv')
exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# print(exampleData)
# print(exampleData[0][0])

# for循环遍历
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

exampleFile.close()

# Write对象
outputFile = open('D:\\Virtual\\PythonLearn\\chapter14\\outputFile.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# 自动转义'Hello, World!'字符串
outputWriter.writerow(['Hello, World!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.1415926, 4])
outputFile.close()

# delimiter和lineterminator关键字参数
# delimiter:
# lineterminator关键字参数
csvFile = open('D:\\Virtual\\PythonLearn\\chapter14\\example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')

csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])

csvFile.close()


# json模块
import json
# json数据类型包括：字符串、整型、浮点型、布尔型、列表、字典和NoneType
# 布尔型True必须写为true，否则就会报错
stringOfJsonData = '{"name":"Zophie", "isCat":true, "miceCaught":0, "felineIQ":null}'
# 用loads()函数读取json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)
# 将dumps函数写出JSON,它表示“dump string”，而不是“dumps”
pythonValue = {'isCat':True, 'miceCaught':0, 'name': 'Zophie', 'felineIQ':None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)