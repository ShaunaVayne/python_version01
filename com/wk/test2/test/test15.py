# 反向迭代
# list1 = [1,2,3,4,5]
# for num in list1:
#     print(num,end=' ')
# for num2 in reversed(list1) :
#     print(num2,end=' ')
# class Countdown :
#     def __init__(self,start):
#         self.start = start
#
#     def __iter__(self):
#         n = self.start
#         while n > 0 :
#             yield n
#             n -= 1
#
#     def __reversed__(self):
#         n = 1
#         while n <= self.start :
#             yield n
#             n += 1;
#
#
# for pp in Countdown(20) :
#     print(pp)

names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]

dict1 = dict(zip(names, ages))
print(dict1)