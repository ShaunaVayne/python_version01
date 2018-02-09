#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# udp 客户端代码

# 创建socket
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'wankgun',b'wangming',b'vayne'] :
    # 发送数据
    s.sendto(data,('127.0.0.1',9999))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))
s.close()
