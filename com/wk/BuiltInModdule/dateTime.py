# py处理日期和时间的标准库
from datetime import datetime

now = datetime.now()
print(now)

# 获得指定时间
dt = datetime(2015, 12, 25, 23, 11, 11)
print(dt)

timestamp1 = datetime.now().timestamp()
print(timestamp1)

fromordinal = datetime.fromtimestamp(1515997461.253312)
print(fromordinal)

# str与datetime之间的转换
# 1.str-->datetime  strptime
strptime = datetime.strptime('2017-12-10 19:20:20', '%Y-%m-%d %H:%M:%S')
print(strptime)
# 2.datetime->str格式化    strftime
now__strptime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now__strptime)
