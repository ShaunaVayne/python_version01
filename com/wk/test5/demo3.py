# 枚举类
from enum import Enum, unique
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 如上就获得了Month的枚举类
# for name, member in Month.__members__.items() :
#     print(name, '=>', member, ',' ,member.value)

# 自定义枚举类
@unique
class week(Enum) :
    sun = 0
    mon = 1
    tue = 2
    wed = 3
    thr = 4
    fri = 5
    sat = 6
# 访问枚举类
d1 = week.mon
print(d1.value)
print(week.thr.value)
print(week(2))