#! python3
# chapter10 调试

# 抛出异常
# 抛出异常使用raise语句

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Hight must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4),('0', 20, 5),('x', 1, 3),('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))


# 取得反向跟踪的字符串
from math import factorial
import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('D:\\Virtual\\PythonLearn\\chapter10\\errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())     # traceback.format_exc()得到反向跟踪的字符串
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

# 断言
# 当条件时False时显示字符串
# podBayDoorStatus我们的程序依赖于它是'open'，才能按照期望工作。通过快速失败，快速定位到缺陷代码
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open"'
# podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open"'

# 在交通灯模拟中使用断言
# 代表路口信号灯的数据结构是一个字典，以'ns'和'ew'为键，分别表示南北向和东西向的信号灯。这些键的值可以是'green'、'yellow'、'red'
mark_2nd = {'ns' : 'green', 'ew' : 'red'}
mission_16th = {'ns' : 'red', 'ew' : 'green'}
import time

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            print(stoplight)
            time.sleep(7)   # 绿灯时间7秒           
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            print(stoplight)
            time.sleep(3)   # 黄灯时间3秒            
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            print(stoplight)
            time.sleep(7)   # 红灯时间7秒
            stoplight[key] = 'green'
        assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)

# switchLights(mark_2nd)

# 日志
import logging
# 将日志记录到文件 filename='D:\\Virtual\\PythonLearn\\chapter10\\myProgramlog.txt',取消此参数，将打印到屏幕上
logging.basicConfig(filename='D:\\Virtual\\PythonLearn\\chapter10\\myProgramlog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# 禁用日志
# logging.disable(logging.CRITICAL)
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total
print(factorial(5))
logging.debug('End of program')

# 日志级别
# DEBUG logging.debug() 最低级别。用于小细节。通常只有在诊断问题时，你才会关心这些消息
# INFO  logging.info()  用于记录程序中一般事件的信息，或确认一切工作正常
# WARNING logging.warning() 用于表示可能的问题，它不会阻止程序工作，但将来可能会
# ERROR logging.error() 用于记录错误，它将导致程序做某事失败
# CRITICAL logging.critical() 最高级别。用于表示致命的错误，它导致或将导致程序完全停止工作
logging.debug('Some debugging details.')
logging.info('The logging model is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
