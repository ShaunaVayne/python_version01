#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
def application(envirson, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    body = '<h1>Hello, %s</h1>' %(envirson['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]