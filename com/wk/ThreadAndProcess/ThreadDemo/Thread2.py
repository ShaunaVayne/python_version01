# 1.Lock机制
# 多进程和多线程不同在于,多进程中, 同一个变量,各自有一份拷贝存在与每个进程中, 互不影响,而多线程中, 同一变量是由所有线程共享的,
# 所以任一变量都可以被任何一个线程修改,即产生java中的多线程安全
# java的思想, 所有的线程享有同一片内存空间(这个内存并不是栈内存,确实对于每一个线程都有一个栈内存来存储本地数据)

# 定义银行存款数
import threading

balance = 0

def change_it(n):
    # 先存后取, 结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # 1.先获取锁
        lock.acquire()
        try :
            change_it(n)
        finally:
            # 2.一定要释放锁
            lock.release()

t1 = threading.Thread(target= run_thread, args=(5,))
t2 = threading.Thread(target= run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# Ending : lock总结
# 为确保最终的结果执行正确, 需给方法上锁, 当Thread t1获得锁的时候,其他Thread t2就不能执行该方法, 形成阻塞效果, 只有当t1执行
# 完毕,同时锁释放才能执行t2, 锁是唯一的, 无论线程多少个, 都能保证结果的唯一性, threading.Lock()获取, 这个锁是方法级别的吗?\

# python多线程总结:
# python解释器由于设计时有GIL全局锁,导致了多线程无法利用多核, 多线程的并发在python只是一个美丽的梦
# GIL锁:任何python线程执行前, 必须先获得GIL锁, 然后么执行100条字节码, 解释器就自动释放GIL锁, 让别的线程有机会执行. 这个GIL全局
# 锁实际上把所有线程执行的代码都上了锁, 所以, 多线程在python中只能交替进行,即使100个线程跑在100核的cpu上, 也只能用到1个核.

