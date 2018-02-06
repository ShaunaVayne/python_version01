# 多线程环境下,每个线程有自己的数据,一个线程使用自己的局部变量比使用全局变量好, 不会影响其他线程, 但是存在的问题是函数调用的时候传递值的问题
import threading
# 创建全局的ThreadLocal对象
loacl_school = threading.local()
def process_student():
    # 获取当前线程关联的Student
    student = loacl_school.student
    print('hello %s in (%s)' %(student, threading.current_thread().name))
def process_thread(name):
    # 绑定Thread_local的student:
    loacl_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Wangkun',) , name= 'Thread_A')
t2 = threading.Thread(target= process_thread, args=('Wangmingming',) , name= 'Thread_B')

t1.start()
t2.start()
t1.join()
t2.join()


