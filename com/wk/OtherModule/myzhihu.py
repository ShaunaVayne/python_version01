#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 模拟知乎登录
# gg,发现并不能用
import os
import requests
import time
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
headers = {
    'Host' : 'www.zhihu.com',
    'Referer' : 'https://www.zhihu.com/',
    'User-agent' : user_agent
}

# step1:构造用于网络请求的session
session = requests.Session()

# step2:获取xsrf-token
indexUrl = 'https://www.zhihu.com'
homeresponse = session.get(url=indexUrl, headers=headers)
homesoup = BeautifulSoup(homeresponse.text, 'html.parser')
xsrfinput = homesoup.find('input', {'name': '_xsrf'})
xsrfvalue = xsrfinput['value']
print('获取的xsrf_token为:', xsrfvalue)

# step3:获取验证码文件
randomtime = str(int(time.time() * 1000))
captchaurl = 'https://www.zhihu.com/captcha.gif?r='+randomtime+'&type=login'
captchresponse = session.get(url=captchaurl, headers=headers)
with open('checkcode.gif', 'wb') as f:
    f.write(captchresponse.text)
    f.close()
captchdata = input('请输入验证码:')
print(captchdata)

# step4:开始登陆
headers['X-Xsrftoken'] = xsrfvalue
headers['X-Requested-With'] = 'XMLHttpRequest'
loginUrl = 'https://www.zhihu.com/login/email'
postdata = {
    '_xsrf' : xsrfvalue,
    'email' : 'ahaqwjwk@163.com',
    'password' : '3g2,eday726'
}
loginResponse = session.post(url=loginUrl, headers=headers, data=postdata)
print('服务器响应的状态码:', loginResponse.status_code)
print(loginResponse.json())

# step5.1:验证码输入问题导致失败:可能是因为session中对于验证码的请求过期导致
if loginResponse.json()['r'] == 1:
    # step5.2:重新输入验证码,再次运行代码正常. 也可以理解为可以在第一次不输入验证码,或者输入了一个错误的验证码,只有第二次是有效的
    randomtime = str(int(time.time() * 1000))
    captchaurl = 'https://www.zhihu.com/captcha.gif?r='+randomtime+'&type=login'
    captchresponse = session.get(url= captchaurl, headers = headers)
    with open('checkcode.gif', 'wb') as f:
        f.write(captchresponse.text)
        f.close()
    os.startfile('checkcode.gif')
    captchdata = input('请输入验证码:')
    print(captchdata)

    postdata['captchdata'] = captchdata
    loginResponse = session.post(url=loginUrl, headers=headers, data=postdata)
    print('服务器响应',loginResponse.status_code)
# step6:保存登录的cookie信息
session.cookies.save()
# step7:判断是否登录成功
profileurl = 'https://www.zhihu.com/settings/profile'
profileresponse = session.get(url=profileurl, headers= headers)
print('profil页面响应状态码',profileresponse.status_code)
profilesoup = BeautifulSoup(profileresponse.text, 'html.parser')
div = profilesoup.find('div', {'id', 'rename-section'})
print(div)


