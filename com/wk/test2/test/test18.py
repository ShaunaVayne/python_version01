# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3])
# print(L[:3])
# print(L[1:3])
# print(L[-2:-1])

L = list(range(100))
print(L[:10])
print(L[-10:])
# 前10个每两个取一个
print(L[:10:2])
print(L[::5])

print((0,1,2,3,4,5)[:3])

print('ABCDEFG'[:3])

print('ABCDEFG'[::2])

# list实现类似java的下标,使用内置对象enumerate可以把一个list变成索引元素对
list1 = ['A','B','C']
res = enumerate(list1)
print(res)
for i,value in enumerate(list1) :
    print(i,value)  
