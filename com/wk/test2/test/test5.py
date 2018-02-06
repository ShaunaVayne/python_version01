# set = set([123, 456, 890,890])
# print(set)
# set.add(345)
# print(set)
# set.remove(123)
# print(set)

set1 = set('hello')
set2 = set(['p','y','y','h','o','n'])
set3 = set1 & set2
print("\n交集set3")
print(set3)

set4 = set1 | set2
print("\n并集set4")
print(set4)

set5 = set1 - set2
set6 = set2 - set1
print("\n差集")
print(set5)
print(set6)