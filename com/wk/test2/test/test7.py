# -*-coding:utf-8-*-
# 1-100的和
count = 1
sum = 0
while (count <= 100) :
    sum += count
    count += 1
print(sum)

# 和大于1000跳出循环
count2 = 1
sum2 = 0
while (count2 <= 100) :
    sum2 += count2
    if sum2 >= 1000:
        break
    count2 += 1
print(sum2)

# 求1-100的奇数和
count3 = 1
sum3 = 0
while count3 <= 100:
    if count3 % 2 == 0 : # 双数跳过输出
        count3 += 1
        continue
    sum3 += count3
    count3 += 1
print(sum3)

# while后面也可加else
count4 = 0
while count4 < 5 :
    print(count4)
    count4 += 1;
else :
    print(count4)