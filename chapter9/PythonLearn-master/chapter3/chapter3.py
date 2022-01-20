# Collatz Sequence(序列)
# 编写一个名为collatz()的函数，它有一个名为number的参数，如果参数是偶数
# 那么collatz()就打印出number//2，并返回该值。如果number是奇数，collazt()就打印并返回3*number-1
# 然后编写一个程序，让用户输入一个整数，并不断对这个数调用collatz。

# 直到函数返回1，(令人惊奇的是，这个序列对于任何整数都有效，利用这个序列，你迟早会得到1！
# 即使数学家也不能确定为什么。你的程序在研究所谓的“collatz序列”，它有时候被称为“最简单的、不可能的数学问题”)。
# 记得input()的返回值用int()函数转成一个整数，否则它会是一个字符串

# 提示：如果number%2==0，整数number就是偶数，如果number%2==1，它就是奇数

# def collatz(number):
#     if number%2==0:
#         print(number//2)
#         return number//2
#     else:
#         print(3*number+1)
#         return(3*number+1)


# if __name__ == "__main__":
#     print("Please input a integer:")
#     inputNumber = int(input())
#     inputNumber = collatz(inputNumber)
#     while(True):
#         if inputNumber == 1:
#             break
#         else:
#             inputNumber = collatz(inputNumber)

# 递归调用
# def collatz(number):
#     if number%2==0:
#         print(number//2)
#         if number//2 != 1:
#             collatz(number//2)
#     else:
#         print(3*number+1)
#         collatz(3*number+1)

# if __name__ == "__main__":
#     print("Please input a integer:")
#     inputName = int(input())
#     collatz(inputName)

# 输入验证
# 在前面的项目中添加try和except语句，检测用户是否输入了一个非整数的字符串。正常情况下，
# int()函数在传入一个非整数字符串时，会产生ValueError错误，比如int('puppy')。在except子句中，
# 向用户输出一条信息，告诉他们必须输入一个整数
def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return(3*number+1)


if __name__ == "__main__":
    print("Please input a integer:")
    
    try:
        inputNumber = int(input())
        inputNumber = collatz(inputNumber)
        while(True):
            if inputNumber == 1:
                break
            else:
                inputNumber = collatz(inputNumber)
    except:
        print("Please input a integer:")


