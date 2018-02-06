# Base64是一种用64个字符来表示任意二进制数据的方法

import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)

# I dont't know why my code hava be a error is that AttributeError: module 'base64' has no attribute 'b64encode'?
# And the module for struct have a same issue.