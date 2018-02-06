from functools import *
def test(a,b,f) :
    return f(a) + f(b)
# print(test(2,-9,abs))

def f(x) :
    return x * 2
r = map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))

def fn(x, y) :
    return x + y
# print(reduce(fn,[1,3,5,7,9]))

def fn1(x, y) :
    return x * 10 + y
# print(reduce(fn1,[1,3,5,7,9]))

def char2Num(s) :
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def fn2(x, y) :
    return x * 10 + y
# print(reduce(fn2,map(char2Num,'13579')))

# 整理成一个函数, 有str转为int类型:
def my_function(s) :
    def fn3(x, y) :
        return x * 10 + y
    def char2Num(s) :
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn3,map(char2Num,s))
# print(my_function('1893'))

# 利用lambda表达式进行优化:
def my_function_2(s) :
    def char2Num(s) :
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(lambda x,y : x * 10 + y,map(char2Num,s))
# print(my_function_2('7890'))

def test2(s) :
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# for i in map(test2,'234') :
#     print(i)
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name) :
    return name.capitalize()
s = ['adam','LISA','parK']
S = map(normalize,list(s))
# print(list(S))

def normalize2(name) :
    res = ''
    for s in range(len(name)) :
        if s == 0 :
            res += name[s].upper()
        else :
            res += name[s].lower()
    return res
L1 = ['adam', 'LISA', 'barT']
# print(list(map(normalize2,L1)))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(l) :
    def f(x, y) :
        return x * y
    return reduce(f,l)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456:
def str2float(s) :
    pointIndex = s.index('.')
    def fn(x, y) :
        return x * 10 + y
    def char2Num(s) :
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}[s]
    return reduce(fn, map(char2Num, s[:pointIndex]))+(0.1**pointIndex)*reduce(fn, map(char2Num, s[pointIndex+1:len(s)]))
print('str2float(\'123.456\') =', str2float('123.456'))