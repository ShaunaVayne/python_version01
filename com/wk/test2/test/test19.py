# print([x * x for x in range(1,11)])
# print([x * x for x in range(1,11) if x % 2 == 0])
# 使用两层循环生成全排列
res = [m + n for m in 'ABC' for n in 'XYZ']
# print(res)
dict1 = {'x': 'A', 'y': 'B', 'z': 'C'}
# for x , y in dict1.items() :
#     print(x , '=', y)

#   把一个list中所有字符变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
res2 = [ s.lower() for s in L]
# print(res2)

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：L1 = ['Hello', 'World', 18, 'Apple', None] 期待输出: ['hello', 'world', 'apple']
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)