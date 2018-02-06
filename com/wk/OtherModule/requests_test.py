#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 访问一个页面
from pip._vendor import requests

# 1.带参数的url,传入dict作为params
r = requests.get('https://www.douban.com/search',params= {'q':'python','cat':'1001'})
print(r.url)
print(r.status_code)
print(r.content)

# 2.对于特定类型的响应,比如json,可以直接获取
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

# 3.需要传入一个header时,传入一个dict作为header参数
r = requests.get('https://www.douban.com/',headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.url)
print(r.text)

# 4.对于post请求
post = requests.post('https://accounts.douban.com/login',
                     data={'form_email': 'ahaqwjwk@163.com', 'form_password': '3g2,eday726'})
print(post.url)
print(post.text)
print(post.status_code)
