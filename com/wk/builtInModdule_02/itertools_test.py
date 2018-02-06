#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# itertools提供了用于操作对象迭代的函数
import itertools

# itertools_count = itertools.count(1)
# for n in itertools_count :
#     print(n)

# cycle = itertools.cycle('ABC')
# for c in cycle:
#     print(c)

# 如上count,cycle两个函数都会无限循环当前对象
print('--------------------------------')

repeat = itertools.repeat('ab', 3)
for r in repeat :
    print(r)

# repeat函数可以限制循环次数

itertools_count = itertools.count(1)
itertools_takewhile = itertools.takewhile(lambda x: x <= 10, itertools_count)
print(list(itertools_takewhile))

# chain()将一组对象串联
for i in itertools.chain('abc','xyz') :
    print(i)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA') :
    print(key, list(group))