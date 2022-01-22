#! python3
# 调试硬币抛投
# 下面程序意图是一个简单的硬币抛掷猜测游戏。玩家有两次猜测机会（这
# 是一个简单的游戏）。但是，程序中有一些缺陷。让程序运行几次，找出缺陷，使
# 该程序能正确运行
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0,1) # 0 is tails, 1 is heads
if toss == guess:
#if ('heads', 'tails')[toss] == guess:    
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    #toss = random.randint(0,1)
    if toss == guess:
    #if ('heads', 'tails')[toss] == guess:
        print('You got it!')
    else:
        print('Nope.You are really bad at this game.')

# 不用调试即可发现一个编程上的逻辑问题
# 假设Guess第一次输入的是tails，结果随机的toss却是heads
# 第二次Guess输入后没有重新toss随机赋值，还是上次的，你输入tails即可通过
# 修改方法在第二次输入后，toss变量必须重新随机赋值

# 调试发现guess变量是heads，toss变量是0，
# 注释部分是修改后的部分