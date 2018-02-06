# 函数
# def sum(sum1, sum2):
#     "两数之和"
#     return sum1 + sum2
#print(sum(2,4))

# b = 1
# def changeNum(b) :
#     b = 1000
#     return b
# b = changeNum(b)
# print(b)


# def changeNum(b) :
#     print("传入之前的值{}".format(b))
#     b = 100
#     print("传入之后的值{}".format(b))
# b = 1
# changeNum(b)
# print("最后输入的值{}".format(b))

# def sum (sum1, sum2):
#     # 两数之和
#     if not (isinstance(sum1,(int, float)) and isinstance(sum2,(int,float))) :
#         raise TypeError('参数类型错误')
#     return sum1 + sum2
# print(sum(1,3.4))

# def divsion(num1 , num2) :
#     #求商和余数
#     a = num1 % num2
#     b = (num1 - a) / num2
#     return a,b,"hah"
# print(divsion(102,3))

# def print_user_info(name, age, sex='男') :
#     # 打印信息
#     print('昵称{}, 年龄{}, 性别{}'.format(name,age,sex))
# print_user_info('刘佳',20,'女')
# print_user_info('王琨',22)

# 如果 b 是一个 list ，可以使用 None 作为默认值
# def print_info(a, b = None) :
#     if b is None :
#         b = []
#     return ;
#
# def print_info2(a, b = []) :
#     return;

# def print_info(a, b = None) :
#     if b is None:
#         b = []
#         print(b)
#     return b;
# result = print_info(1)
# result.append('error')
# print_info(2)

# def print_info(a, b) :
#     if b is object() :
#         print('b没有传入任何值')
# print_info(2)

# def print_info_user(name, age, sex = '男') :
#     print('昵称{}'.format(name),end=' ')
#     print('年龄{}'.format(age),end=' ')
#     print('性别{}'.format(sex),end=' ')
#     return ;
# print_info_user(name='王琨',age=20,sex='男')
# print_info_user(name='刘佳',sex='女',age=22)

# def print_info_user(name, age, sex='男', *hobby) :
#     print('昵称：{}'.format(name), end=' ')
#     print('年龄：{}'.format(age), end=' ')
#     print('性别：{}'.format(sex), end=' ')
#     print('爱好：{}'.format(hobby))
# # 调用函数
# print_info_user('王琨',23,'男', '打篮球','打羽毛球','跑步')

# def print_info_user(name, age, sex='男', ** hobby) :
#     print('昵称：{}'.format(name), end=' ')
#     print('年龄：{}'.format(age), end=' ')
#     print('性别：{}'.format(sex), end=' ')
#     print('爱好：{}'.format(hobby))
#     return ;
# print_info_user(name='王琨',age=20,sex='男',hobby2 =('篮球','足球'))

def print_info_user(name, *, age, sex='男') :
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return;
print_info_user(name='王琨',age=20)
# 这种写法会报错,因为age,sex这两个参数强制使用关键字参数
# print_info_user('刘佳',20,'女')
# 如下写法就不会报错, 因为*在age和sex前, 所以age和sex两个参数为强制型参数
print_info_user('刘佳',age=20,sex='女')


