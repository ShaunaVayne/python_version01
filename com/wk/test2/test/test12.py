# list生成式 列表生成式
# 一句话生成乘法表
# print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))
list1 = [x * x for x in range(1, 11)]
print(list1)

list2 = [i * i for i in range(1, 11) if i % 2 == 0]
print(list2)

list3 = [ (a+1, b+1) for a in range(5) for b in range(5)]
print(list3)
