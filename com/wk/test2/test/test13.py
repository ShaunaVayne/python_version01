# 生成器
# gen = (x * x for x in range(5))
# while True :
#     try :
#         print(next(gen))
#     except StopIteration:
#         break

# def my_function() :
#     for i in range(10) :
#         yield i
# print(my_function())

# -*- coding: UTF-8 -*-
# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# 引用函数
# for x in fibon(1000000):
#   print(x , end = ' ')
for x,y in [('a',1),('b',2),('c',3)]:
    print(x, y)

l = [1];
l.append(0);
print(len(l))



