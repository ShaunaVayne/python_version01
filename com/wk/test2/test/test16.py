# 体重除以身高的平方
# a = input('请输入身高:')
# a = int(a)
# b = input('请输入体重:')
# b = int(b)
# c = b / (a * a)
# if c < 18.5 :
#     print('过轻')
# elif 18.5 <= c < 25 :
#     print('正常')
# elif 25 <= c < 28 :
#     print('过重')
# elif 28 <= c < 32 :
#     print('肥胖')
# else:
#     print('严重肥胖')

def my_function(x) :
    if not isinstance(x,(int,float)) :
        raise TypeError('false param type')
    if x >= 0 :
        return x
    else :
        return -x

# print(my_function(-9))

b = 5
print(b ** 2)
