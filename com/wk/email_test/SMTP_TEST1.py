#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 发送纯文本邮件
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('你好, 这是一封来自python发送的邮件','plain','utf-8')
# 传入'plain'表示纯文本,最终的MIME就是'text/plain'
# 通过SMTP发送邮件
from_email_addr = 'ahaqwjwk@163.com'
email_pwd = '1234qaQA'
to_email_addr = '15981960755@163.com'
# SMTP服务器地址
smtp_server = 'smtp.163.com'

server = smtplib.SMTP(smtp_server, 25)  #默认协议端口是25
server.set_debuglevel(1)
server.login(from_email_addr, email_pwd)
server.sendmail(from_email_addr, [to_email_addr], msg.as_string())
server.quit()


