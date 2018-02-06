# 进程之间的通信, 以Queue为例
import random
from multiprocessing import Process, Queue

import os

import time


def write(args):
    print('Process to write: %s'% os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' %value)
        args.put(value)
    time.sleep(random.random())

def read(args):
    print('Process to read: %s' % os.getpid())
    while True:
        value = args.get(True)
        print('Get %s from queue.' %value)


if __name__ == '__main__':
    # 父进程创建Queue,并传给各个子进程
    q = Queue()
    pw = Process(target= write, args=(q,))
    pr = Process(target= read, args=(q,))
    # 启动子进程pw,写入:
    pw.start()
    # 启动子进程pr,读取:
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环, 无法等待他结束, 只能强行终止
    pr.terminate()

