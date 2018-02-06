# python标准库提供了两个模块,_thread和threading,_thread是低级模块,threading是高级模块,对_thread进行了封装,
# 启动一个线程与java类似
import threading

import time


def loop():
    print('thread %s is running' % threading.current_thread().name)
    n = 0
    while n < 5 :
        n += 1
        print('thread %s >>> %s' %(threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is running...' % threading.current_thread().name)

print('thread %s running.' % threading.current_thread().name)
t = threading.Thread(target = loop, name='')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 任何进程启动都会默认启动一个线程,称为主线程,主线程又可以启动新的线程,pythond的threading模块有一个current_thread()函数,返回当前线程的实例
# 主线程的实例名字为MainThread, 子线程名字在创建的时候指定, 无特定意义, 如果不指定, 则python用thread_1, thread_2代替

