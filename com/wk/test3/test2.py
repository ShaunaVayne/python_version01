def lazy_sum(*args) :
    def _sum() :
        start = 0
        for n in args :
            start = start + n
        return start
    return _sum

f1 = lazy_sum(1,2,3,4)
f2 = lazy_sum(1,2,3,4)
# print(f1 == f2)


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())

def count() :
    def f(j) :
        def g() :
            return j * j
        return g
    fs = []
    for i in range(1, 4) :
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())

a = lambda x : x * x
print(a(5))
