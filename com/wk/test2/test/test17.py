import math

def quadratic(a,b,c):
# ax^2+bx+c=0
# a为0不是一元二次方程,不合题意
    if a == 0 :
        print('参数错误!!!')
    else :
        data = b * b - 4 * a * c
        if data > 0 :
            # 方程有两个不相等的根
            x1 = (-b + math.sqrt(data)) / (2 * a)
            x2 = (-b - math.sqrt(data)) / (2 * a)
            print('此方程有两个不等实根：x1=%s x2=%s' % (x1, x2))
            return x1 , x2
        elif data == 0 :
            # 方程有两个相等的根
            print('此方程有两个相等实根：x1=x2=%s' % (-b / (2 * a), -b / (2 * a)))
            return -b / (2 * a)
        else :
            return None
# result = quadratic(1,2,-1)
# print(result)

def calc(*nums) :
    sum = 0
    for num in nums :
        sum = sum + num * num
    return sum

list1 = [1,2,3]
# print(calc(*list1))

#   ---------
#   命名关键字参数需要一个特殊分隔符*, * 后面的参数被视为命名关键字参数
def person(name,age, *,city,job) :
    print(name,age,city,job)
# person('Jack', 24, city='Beijing', job='Engineer')

def person2(name,age,*,city='beijing',job) :
    print(name,age,city,job)
# person2('wangkun','22',job='student')


def f1(a, b, c=0, *args, **kw) :
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw) :
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# f1(1,2)
#
# f1(1,2,c=3)
#
# f1(1,2,3,'a','b')
#
# f1(1,2,3,'a','b',x=99)
#
# f2(1,2,d=90,ext=None)

args = (1,2,3,4)
kw = {'d' : 44, 'x' : '#'}
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)

args = (1,2,3)
kw = {'d' : 88, 'x' : '#'}
# f2(*args, **kw)

# -*- coding: utf-8 -*-
def move(n, a, b, c):
    if n == 1:
        print('{a} >> {c}'.format(a=a,c=c))
        return
    move(n-1,a,c,b)
    print('{a} >> {c}'.format(a=a,c=c))
    move(n-1,b,a,c)
if __name__ == '__main__':
    move(3,'A','B','C')