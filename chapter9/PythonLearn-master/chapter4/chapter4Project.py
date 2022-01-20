# project1：逗号代码
# 假定有下面列表
spam = ['apple','banansa','tofu','cats']
# 编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所有表项，
# 表项之间以逗号和空格分隔，并在最后一个表项之前插入and。例如，
# 将前面的spam列表传递给函数，将返回值'apples，bananas，tofu，and cats'。
# 但你的函数应该能够处理传递给它的任何列表
def ListToStr(listVar):
    sizeListVar = len(spam)
    strVar = ""
    for item in range(sizeListVar - 1):
        strVar += (listVar[item]+",")
    strVar += ("and " +listVar[-1])
    return strVar



# project2:字符图网格
# 假定有一个列表的列表，内层列表的每个值都是包含一个字符的字符串，像这样：
grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]
# 你可以认为grid[x][y]是一幅“图”在x、y坐标处的字符，该图由文本字符组成，
# 原点(0,0)在左上角，向右x坐标增加，向下y坐标增加。
# 复制前面的网格值编写代码用它打赢出图像
# ..00.00..
# .0000000.
# .0000000.
# ..00000..
# ...000...
# ....0....
# 提示：
# 你需要使用循环嵌套循环，打印出grid[0][0]，然后grid[1][0]，然后grid[2][0]，
# 以此类推，直到grid[8][0],这就完成第一行，所以接下来打印换行。然后程序将打印出grid[0][1]，
# 然后grid[1][1]，然后grid[2][1]，以此类推，程序最后将打印出grid[8][5].
# 
# 而且，如果你不希望在每次print()调用后都打印换行，记得想print()传递end关键字

def TwoListStrIterator(grid):
    x = len(grid)
    y = len(grid[1])
    for i in range(y):
        printStr = ""
        for j in range(x):
            printStr += grid[j][i]
        print(printStr)

if __name__ == "__main__":
    print(ListToStr(spam))
    TwoListStrIterator(grid)