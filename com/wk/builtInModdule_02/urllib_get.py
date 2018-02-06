#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 模拟发送get请求,需求request对象
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

request_request = request.Request('https://www.baidu.com/')
request_request.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(request_request) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s , %s' %(k, v))
    print('data:', f.read().decode('utf-8'))

