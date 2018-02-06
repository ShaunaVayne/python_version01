import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def calc_pwd(pwd):
    md_ = hashlib.md5()
    md_.update(pwd.encode('utf-8'))
    return md_.hexdigest()


def login() :
    while True:
        user = input('welecome to login to the webSite, please input your username:')
        pwd = input('input your password to loging:')
        if user not in db.keys() :
            print('user is undefined')
            return False
        elif calc_pwd(pwd) == db[user] :
            print('loging success')
            return  True
        elif calc_pwd(pwd) != db[user] :
            print('loging failed')
            return False

if __name__ == '__main__' :
    login()