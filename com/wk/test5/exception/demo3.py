# 1.断言  assert代替print()
# assert的意思是, 表达式 n != 0应该是True, 否则根据程序逻辑, 后面的的代码会提示错误, 如果断言失败, 会抛出AssertionError错误
import logging
logging.basicConfig(level=logging.INFO)


def foo(param):
    n = int(param)
    assert n != 0 , 'n is Zero'
    return 10 / n
    pass

def main() :
    print(foo('2'))
# main()

# 2.logging 在导入logging包后,需要进行配置logging.basicConfig(level=logging.INFO), 会将具体的配置打印
s = '2'
n = int(s)
logging.info('n = %d' %n)
print(10 / n)

# 3. 使用pdb.set_trace()手动设置断点, 命令p查看变量,命令c继续运行, 命令行的调试, 可以直接IDE进行debug,java的jdb类似于pdb
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)