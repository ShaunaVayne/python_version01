# 正则表达式
import re

test = '010-12345a'
if re.match(r'^\d{3}\-\d{3,8}$', test) :
    print('ok')
else :
    print('not ok')

# 切分字符串
s = 'a b   c'.split(' ')
print(s)
s2 = re.split(r'[\s\,]+', 'a,b, c  d')
print(s2)
s3 = re.split(r'[\s\,\;]+', 'a,b;; c  d')
print(s3)

ne = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(ne.groups())

t = '19:57:27'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

# 预编译正则表达式
regex = re.compile(r'^(\d{3})-(\d{3,8})$')
# 调用
print(regex.match('010-12345').groups())
print(regex.match('010-98900').groups())
