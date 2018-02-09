#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 底层代码由专门的服务器软件实现,使用py专注于写html文档,不希望接触tcp连接,http原始请求和响应格式,则需要一个统一接口--WSGI: web server gateway interface
def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return ['<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <title>test_wsgi</title> </head> <body> <table> <tr> <th>username:</th> <th><input name="username" type="text"/></th> </tr> <tr> <th>password:</th> <th><input name="password" type="password"/></th> </tr> </table> </body> </html>'.encode('utf-8')]
