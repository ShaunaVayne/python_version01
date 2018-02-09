#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server

from com.wk.web_test.WSGI_TEST import application

server = make_server('', 8889, application)
print('Servring http on port 8889 starting...')
# 监听http请求
server.serve_forever()
