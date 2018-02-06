import os,time,random

from multiprocessing import Process
# 1.macOs下直接调用fork方法创建子进程
# print('Process %s start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am a children process(%s) and my parent process is %s.' %(os.getpid(), os.getppid()))
# else :
#     print('I %s create a process %s.' %(os.getpid(), pid))

# 2.window环境下创建子进程
from multiprocessing.pool import Pool


# def run_proc(name):
#     print('Run children process %s(%s)' %(name, os.getpid()))
# if __name__ == '__main__':
#     print('Parent Process %s..' % os.getpid())
#     p = Process(target= run_proc, args=('test',))
#     print('Children process is start')
#     p.start()
#     p.join()
#     print('Children proces is end')

# 3.如果要批量创建子进程, 使用线程池
# 分析:对Pool对象调用join方法会等待所有子进程执行完毕,调用join()之前必须先close(),同时调用close之后就不能添加新的process了
def long_time_task(name) :
    print('Run task %s(%s)...' %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' %(name, (end - start)))
if __name__ == '__main__':
    print('Parent Process %s.' %os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args= (i,))
    p.close()
    p.join()
    print('All Process is end')

