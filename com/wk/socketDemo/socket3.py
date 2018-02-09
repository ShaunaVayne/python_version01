#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# 客户端程序
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1',9999))
# 接收响应消息
print(s.recv(1024).decode('utf-8'))
for data in [b'this is client',b'Michael',b'Tracy',b'Sarch']:
    # 发送消息
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()