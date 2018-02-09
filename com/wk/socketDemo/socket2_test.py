#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
'''
 服务器网络通信编程:
 服务器进程先绑定一端口进行监听,若某客户端连接过来,即与服务器建立了socket连接,进行通信.
 由于服务器会有大量来自客户端的连接,所以需要区分.一个socket依赖4项:服务器地址,服务器端口,客户端地址,客户端端口来确定唯一的socket.
 服务器还需要响应多个客户端的请求,则每个连接都需要一个新的进程或者线程处理
'''
import socket

# 创建socket
import threading

import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1',9999))
# 调用listen()方法监听端口,传入参数为指定等待连接的最大数量
s.listen(5)
print('waiting for connection...')
# 服务器程序通过一个死循环接收来自客户端的连接,accept()会等待并返回一个客户端的连接

def tcplink(sock, addr):
    print('accept new connection from %s:%s...' % addr)
    sock.send(b'welcome! this is server')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        print(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection from %s:%s closed.' %addr)

while True:
    # 接收一个新连接
    sock, addr = s.accept()
    # 起另一线程来处理tcp连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()