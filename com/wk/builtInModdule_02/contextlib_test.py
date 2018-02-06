#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-

# 1.说明, 实现上下文管理是通过__enter__和__exit__两个方法实现的,类似java过滤器的init和destory方法, 类加载开始和结束之前分别执行, 实现Filter接口
# 并且对于任何对象, 只要实现了上下文管理, 就可以用于with语句, 如下
from contextlib import contextmanager, closing
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class Query(object):
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print('begin')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type :
            print('error')
        else:
            print('end')
    def query(self):
        print('query about %s...' % self.name)

with Query('bob') as b:
    b.query()


# 2.@contextmanager
# 编写__enter__和__exit__还是比较麻烦,python提供了contextlib方法, 简写如下:
class Student(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('query about %s...' % self.name)

@contextmanager
def create_query(name) :
    print('begin')
    q = Student(name)
    yield q
    print('end')

with create_query('tom') as t:
    t.query()

# 3.需要某段代码执行前后自动执行特定代码,也能用@contextmanager
@contextmanager
def tag(name) :
    print('<%s>' % name)
    yield
    print('</%s>' % name)
with tag('h1'):
    print('hello')
    print('world')

# 4.closing
# 如果一个对象没有实现上下文,则不能用于with语句,此时可以用closing()将该对象变成上下文对象
with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)

