# Project1:好玩游戏的物品清单
# 你在创建一个好玩的视频游戏。用于对玩家物品清单建模的数据结构是一个字典。
# 其中键是字符串，描述清单中的物品，值是一个整形值，说明玩家有多少该物品。
# 例如，字典值{'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
# 意味着玩家有1条绳索、6个火把、42枚金币等
#
# 写一个名为displayInventory()的函数，它接受任何可能的物品清单，并显示如下：
# 提示：你可以使用for循环，遍历字典中所有的键
stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for k,v in inventory.items():
        print(str(k) + ': ' + str(v))
        total += v
    print('Total number of items: ' + str(total))

# Project2：列表到字典的函数，针对好玩游戏物品清单
# 假如征服一条龙的战利品表示为这样的字符串列表：
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
# 写一个名为addToInventory(inventory,addedItems)的函数，其中inventory参数
# 是一个字典，表示玩家的物品清单(像前面项目一样)，addedItems参数是一个列表，
# 就像dragonLoot。
# addToInventory()函数应该返回一个字典，表示更新过的物品清单。请注意，列表可以包含多个同样的项
def addToInventory(inventory,addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
    for i in addedItems:
        inventory[i] += 1
        
if __name__ == '__main__':
    addToInventory(stuff,dragonLoot)
    displayInventory(stuff)
