#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 对https://api.douban.com/v2/book/2129650进行抓取
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# get
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('status:', f.status, f.reason)
    for k, v in f.getheaders() :
        print('%s : %s' %(k, v))
    print('data:', data.decode('utf-8'))
# 只是使用request.urlopen()会报如下错误:
# urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:748)>

# 产生如上错误的原因:
#   python2.7.9之后版本引入一个新特性,使用urllib.urlopen一个https会验证ssl证书,
#   当目标使用的是自签名的证书就会报如上错误,
#   解决方法: 全局添加下面的代码:
#           import ssl
#           ssl._create_default_https_context = ssl._create_unverified_context