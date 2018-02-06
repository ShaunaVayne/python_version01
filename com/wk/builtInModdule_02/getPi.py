import itertools


def pi(n) :
    # 1.创建一个奇数列
    itertools_count = itertools.count(1, 2)
    # 2.取该数列的前n项
    itertools_takewhile = itertools.takewhile(lambda x: x <= 2 * n - 1, itertools_count)
    # 3.添加正负符号并用4除
    itertools_cycle = itertools.cycle([4, -4])
    res = []
    for i in itertools_takewhile :
        res.append(next(itertools_cycle)/i)
    return sum(res)

print(pi(100000000))

assert 3.1414 < pi(10000) < 3.1415
print('ok')