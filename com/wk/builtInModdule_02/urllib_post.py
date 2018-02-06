#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 若是模拟post请求,将参数data以bytes的形式传入, 模拟一个登陆功能
from urllib import parse, request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

print('logining is begin')
email = input('email :')
pwd = input('pwd:')
login_data = parse.urlencode([
    ('username',email),
    ('password',pwd),
    ('entry','mweibo'),
    ('savesstate',1),
    ('ec',''),
    ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f :
    print('status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s, %s' %(k, v))
    print('data:', f.read().decode('utf-8'))

