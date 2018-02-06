# for循环
# for x in "hello 你好啊":
#     print(x)

# 遍历10到20之间的数字
# for num in range(10, 20) :
#     for i in range(2,num) :
#         if num % i == 0:
#             j = num / i
#             print("%d 是一个合数" % num)
#             break
#     else :
#         print("%d 是一个质数" % num)

# 打印乘法表
# for i in range(1, 10) :
#     for j in range(1, i+1) :
#         print('{}x{}={}\t'.format(i, j, i * j),end='')
#     print()

# 判断是否是闰年
# year = int(input('请输入一个年份: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 ==0 :
#     print('{0}是闰年'.format(year))
# else:
#     print('{0}不是闰年'.format(year))

for i in range(1,10) :
    for j in range(1, i+1) :
        print('{}x{}={}\t'.format(i,j,i*j),end='')
    print()
