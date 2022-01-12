# Project3：表格打印
# 编写一个名为printTable()的函数，它接受字符串的列表的列表，将它显示在组织良好的表格中，
# 每列右对齐。假定所有内层列表都包含同样数目的字符串。例如：该值可能看起来像这样：
tableData = [['apples','orange','cherries','banana'],
            ['Alice','Bob','Carol','David'],
            ['Dogs','cats','moose','goose']]
# 你的printTable()函数将打印出
#   apples Alice  Dogs
#   orange   Bob  cats
# cherries Carol moose
#   banana David goose
# 提示：你的代码首先必须找到每个内层列表中最长的字符串，这样整列就有足够的宽度以
# 放下所有的字符串。你可以将每一列的最大宽度，保存为一个整数的列表。printTable()函数
# 的开始可以是colWidths = [0] * len(tableData)，这样，colWidths[0]就可以保存
# tableData[0]中最长字符串的宽度，以此类推，然后找到colWidths列表中最大的值，决定
# 将什么整数宽度传递个rjust()字符串方法。
dataSize = []

for i in range(len(tableData)):
    for j in range(len(tableData[0])):
        if j == 0:
            dataSize.append(len(tableData[i][j]))
        else:
            if dataSize[i] < len(tableData[i][j]):
               dataSize[i] = len(tableData[i][j])
               
for i in range(len(tableData[0])):
    dataStr = ""
    for j in range(len(tableData)):
        print(tableData[j][i].rjust(dataSize[j]),end=" ")
    print()
