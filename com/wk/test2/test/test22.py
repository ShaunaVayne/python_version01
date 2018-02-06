def is_odd(n) :
    return n % 2 == 1
a = list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15]))
# print(a)

def not_empty(s) :
    return s and s.strip();
# print(list(filter(not_empty,['A', '', 'B', None, 'C', '  '])))

# 构造一个从3开始的序列, 为一个生成器
def _odd_iter() :
    n = 1
    while True :
        n = n + 2
        yield n

# 定义一个筛选函数
def _not_divisible(n) :
    return lambda  x : x % n > 0

def primes() :
    yield 2
    it = _odd_iter()    #初始序列
    while True :
        n = next(it)    #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n),it)   #构造新序列

# for n in primes() :
#     if n < 100:
#         print(n)
#     else :
#         break

def is_palindrome(n):
    return n and str(n) == str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))

