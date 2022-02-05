#! python3
# time模块
from __future__ import print_function
from ntpath import join
from re import M
import time
from tkinter import W, Y
from winreg import HKEY_LOCAL_MACHINE
print(time.time())
time.sleep(1)
now = time.time()
print(now)
print(round(now))
print(round(now, 2))
print(round(now, 4))

# datetime模块
import datetime
dt = datetime.datetime.now()
print('%s年%s月%s日,%s时%s分%s秒' % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))
print(datetime.datetime.fromtimestamp(time.time()))

helloween2015 = datetime.datetime(2015, 10, 31, 0, 0 ,0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)

print('helloween2015 == oct31_2015 : ' + str(helloween2015 == oct31_2015))
print('helloween2015 > newyears2016 : ' + str(helloween2015 > newyears2016))
print('newyears2016 > helloween2015 : ' + str(newyears2016 > helloween2015))
print('newyears2016 != oct31_2015 : ' + str(newyears2016 != oct31_2015))

# timedelta数据类型，它表示一段时间，而不是一个时刻
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)

dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)    # 生成1000天时间
print(dt + thousandDays)    # 1000天后的现在

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365*30)
print(oct21st)
print(oct21st - aboutThirtyYears)
print(oct21st - (2 * aboutThirtyYears))

# while循环只是每秒检查一次，在2016年万圣节后继续执行后面的程序
halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)

# 将datetime对象转换为字符串
# strftime()指令
# f 表示格式，format
# %Y      带世纪的年份，例如'2014'
# %y      不带世纪的年份，'00'至'99'（1970至2069）
# %m      数字表示的月份，'01'至'12'
# %B      完整的月份，例如'November'
# %b      简写的月份，例如'Nov'
# %d      一月中的第几天，'01'至'31'
# %j      一年中的第几天，'001'至'366'
# %w      一周中的第几天，'0'（周日）至'6'(周六)
# %A      完整的周几，例如'Monday'
# %a      简写的周几，例如'Mon'
# %H      小时（24小时时钟），'00'至'23'
# %I      小时（12小时时钟），'01'至'12'
# %M      分，'00'至'59'
# %S      秒，'00'至'59'
# %p      'AM'或'PM'        %%      就是'%'字符
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

# 将字符串换成datetime对象
# p表示解析，parse
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '15", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))
