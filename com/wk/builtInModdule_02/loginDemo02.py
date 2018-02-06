# 摘要算法加盐值
import hashlib
import random

db = {}


def get_md5(param):
    return hashlib.md5(param.encode('utf-8')).hexdigest()

def register(uName, pwd) :
    db[uName]  = get_md5(pwd + uName + 'the_salt')

class User(object) :
    def __init__(self, uName, pwd):
        self.uName = uName
        self.salt = ''.join([chr(random.randint(48,122)) for i in range(20)])
        self.pwd = get_md5(pwd + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(uName, pwd) :
    user = db[uName]
    return user.pwd == get_md5(pwd + user.salt)

# 测试
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234562')
print('ok')