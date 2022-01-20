# 列表
# 操作：数组、切片、连接、删除、查询、增加、排序、复制
# copy复制列表里面没有嵌套列表的情况 deepcopy复制列表里面有嵌套列表的情况
import copy
spam = ['cat','bat','rat','elephant']
print(spam[0])
print(spam[-1])
print(spam[1:-1])
print("The spam length is:" + str(len(spam)))
print(spam + [1,2,3])
del spam[2]
print(spam)
print('panda' in spam)
print('panda' not in spam)
#print(spam.index('panda'))
print(spam.index('bat'))
spam.append('panda')
print(spam)
spam.insert(3,'chicken')
print(spam)
spam.remove('bat')
print(spam)
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
spamcopy = copy.copy(spam)
print(spamcopy)
spamspam = [['cat','bat','rat','elephant'],[1,2,3,4]]
spamspamdeepcopy = copy.deepcopy(spamspam)
print(spamspamdeepcopy)

# 字符串
name = "Zophie a cat"
print(name)
newName = name[0:7] + "the" + name[8:12]
print(newName)

# 元组
eggs = ("hello",1,2,0.5)
print(eggs)

# 元组和列表转换
eggsList = list(eggs)
print("eggsList type:" + str(type(eggsList)))
spamtuple = tuple(eggs)
print("spamTuple type:" + str(type(spamtuple)))






# 总结：
# 列表是可变数据类型，字符串是不可变数据类型，元组也是不可变数据类型