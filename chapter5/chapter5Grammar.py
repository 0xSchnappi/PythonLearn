# 字典：
# 字典不像列表的下标，字典的索引可以使用许多不同数据类型
# 字典是不排序的
myCat = {'size':'fat','color':'gray','disposition':'loud'}
print(myCat['size'])
# 字典遍历
print("遍历键：")
for i in myCat.keys():
    print(i)
print("遍历值：")
for i in myCat.values():
    print(i)
print("遍历字典：")
for i in myCat.items():
    print(i)
# 检查字典是否存在键或值
print("检查字典是否存在键")
print('size' in myCat.keys())
print('size' not in myCat.keys())
print("检查字典是否存在值")
print('fat' in myCat.values())
print('fat' not in myCat.values())
# get()方法
print("My cat color is " + str(myCat.get('color','Null')) + '.')
print("My cat Length is " + str(myCat.get('length',0)) + '.')
# setdefault()方法
myCat.setdefault('length',0)
print(myCat)
# 漂亮打印
# pprint对于字典本身包含嵌套的列表或字典，pprint.pprint()函数特别有8
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
pprint.pprint(count)
# 井字棋盘
# theBoard = {'top-L':' ','top-M':' ','top-R':' ',
#             'mid-L':' ','mid-M':' ','mid-R':' ',
#             'low-L':' ','low-M':' ','low-R':' '}
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
# 嵌套的字典和列表
allGuests = {'Alice':{'apples':5,'pretzels':12},
            'Bob':{'ham sandwiches':3,'apples':2},
            'Carol':{'cups':3,'apple pies':1}}
def totalBrought(guests, item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought
print('number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests,'apples')))
print(' - Cups ' + str(totalBrought(allGuests,'Cups')))
print(' - Cakes ' + str(totalBrought(allGuests,'Cakes')))
print(' - Ham Sandwiches' + str(totalBrought(allGuests,'ham sandwiches')))
print(' - Apple Pies' + str(totalBrought(allGuests,'apple pies')))