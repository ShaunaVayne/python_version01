# hashlib提供常用的摘要算法,如MD5,SHA1等
# 摘要算法:又称为哈希算法,
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())