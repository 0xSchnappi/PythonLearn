#! python3
# stopwatch.py
# 你的程序需要完成：
# 1.记录从按下回车键开始，每次按键的时间，每次按键都是一个新的“单圈”
# 2.打印圈数、总时间和单圈时间
# 这意味代码将需要完成以下任务
# 1.在程序开始时，通过调用time.time()得到当前时间，将它保存为一个时间戳
# 2.记录圈数，每次用户按下回车键时加1
# 3.用时间戳相减，得到计算流逝的时间
# 4.处理KeyboardInterrupt异常，这样用户可以按Ctrl-C退出

from functools import total_ordering
import time

# Display the Program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()         # press Enter to begin
print('Stsrted')
startTime = time.time()     # get the first lap's start time
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()      # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')

start = time.time()