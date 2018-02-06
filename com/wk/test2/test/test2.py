#-*-coding:utf-8-*-
#-----------------------list的使用----------------------------------
# 1.一个产品，需要列出产品的用户，这时候就可以使用一个 list 来表示
user = ['liangdianshui','twowater','两点水']
print(user)
# 2.如果需要统计有多少个用户，这时候 len() 函数可以获的 list 里元素的个数
tem='%d' %len(user)
print("\n用户数量为"+tem)
print("\n用户数量为"+str(len(user)))
print(len(user))
# 3.此时，如果需要知道具体的用户呢？可以用过索引来访问 list 中每一个位置的元素，索引是0从开始的
print("\n查看具体用户"+user[0]+","+user[1]+","+user[2])
# 4.指定位置添加用户
user.insert(0,"vip用户")
print(user)
# 5.删除末尾用户
user.pop()
print(user)
# 6.删除指定用户
user.pop(2)
print(user)
# 7.单单保存用户昵称好像不够好，最好把账号也放进去
newUser = [['vipUser',1111],['normalUser1',2222],['normalUser2',3333]]
print(newUser)
# 8.迭代
for x in newUser:
    print(x)
