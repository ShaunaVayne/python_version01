#-*-coding:utf-8-*-
# 元组
tuple1 = ('两点水','twowter','liangdianshui',123,456)
tuple2 ='两点水','twowter','liangdianshui',123,456
print(tuple1)
print(tuple2)
# 元组只有一个数据的时候,需要在元素后加上逗号, 不加逗号创建出来的就不是元组了,而是具体某一个值
tuple3 = ('nihao',)
print(tuple3)
print(tuple1[2])
for x in tuple1:
    print(x)