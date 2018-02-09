#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
'''
    tcp是建立可靠的连接,双方通信都是以流的形式发送数据, udp则是面向无连接的协议
    使用udp不需要建立连接,只需要知道对方的ip和端口则可以直接发送数据包
    udp缺点:传送不可靠;优点:比tcp快
'''
import socket

# 创建socket的时候,SOCK_DGRAM指定了此socket是udp类型的,不需要调用listen()方法,接收任何来自客户端的数据
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1',9999))
print('Bind UDP port is 9999')
while True:
    # 接收数据, recvfrom方法返回数据和客户端地址与端口,直接调用sendto()就可以把数据用UDP的协议发给客户端
    data, addr = s.recvfrom(1024)
    print('recevied from %s : %s' % addr)
    s.sendto(b'hello, %s!' % data,addr)
'''
    总结:
    UDP和TCP使用类似,只是不需要建立连接,另外UDP和TCP绑定的端口互不冲突, 即9999端口可以各自绑定
'''

