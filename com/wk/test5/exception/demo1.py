# 1.try函数的机制:
# try :
#     print('try.....')
#     r = 10 / 2
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('exception')
#     print('exception: ' , e)
# finally:
#     print('finnally...')
# print('end')

# 2.非单个异常  注意,如果没有错误发生, 可以在except后面加else语句块,自动执行else, 表示没错误发生
import logging

try :
    print('try...')
    r = 10 / 2
except ValueError as e :
    print('except1,', e)
except ZeroDivisionError as e:
    print('except2', e)
else:
    print('not except')
finally:
    print('finally...')
print('end')

# 小异常都大异常的继承关系, 源码发现:ValueError-->Exception-->BaseException-->object
# 所以最大错误异常为BaseException, 所有的错误都可以有这个异常捕获

# 3.main函数可以直接捕获调用方法的异常, 跟java异常机制类似, 就是不知道会不会打印具体异常信息, 有待考究
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main() :
    try :
        res = bar('2')
        print(res)
    except Exception as  e:
        print('Error',e)
    finally:
        print('End')

# 4. python内置的logging打印错误
def main2() :
    try :
        bar('0')
    except BaseException as e2:
        logging.exception(e2)
    finally:
        print('End')
main2()






