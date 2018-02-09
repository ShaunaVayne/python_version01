#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 带有主题的邮件
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from_email = 'ahaqwjwk@163.com'
email_pwd = '1234qaQA'
to_email = '1035087780@qq.com'
smtp_server = 'smtp.163.com'
# msg = MIMEText('你好, 这是一封来自python发送的邮件', 'html', 'utf-8')
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')


def _from_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


msg['From'] = _from_addr('python爱好者<%s>' % from_email)
msg['To'] = _from_addr('管理员<%s>' % to_email)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_email, email_pwd)
server.sendmail(from_email, [to_email], msg.as_string())
server.quit()
