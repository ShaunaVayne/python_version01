# 迭代
# dict1 = {'a' : 1, 'b' : 2}
# for x in dict1.keys() :
#     print(dict1.get(x))

# 如果一个list里有两个元素, 迭代
# for x,y in [(1,'a'),(2,'b'),(3,'c')] :
#     print(x,y)

# 迭代字符串对象
str1 = 'liangdianshui'
iter1 = iter(str1)
# 迭代list
list1 = [1,3,4]
iter2 = iter(list1)
# 迭代元组
tuple1 = ('1',3,'a')
iter3 = iter(tuple1)
for x in iter1 :
    print(x,end=' ')
print('\n------------------------')
while True:
    try :
        print(next(iter3))
    except StopIteration :
        break

