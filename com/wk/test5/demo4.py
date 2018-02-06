# 使用元类
# 1 type函数定义一个类
def fn (self, name='world1') :
    print('hello %s' %name)
Hello = type('Hello',(object,), dict(hello =fn)) #创建Hello class
h = Hello()
h.hello()
print(type(h))
# 注意点, 使用type函数创建类,需要传入三个参数, 分别为:(1) 函数名;(2)继承的类, 由于python是多重继承,若只有一个父类, 需主要touple单元素的写法;(3)class的方法名称与函数绑定

# 2 metaclass -->元类; 先定义metaclass,则可以创建类,最后创建实例
# eg:利用metaclass给自定义的myList添加一个add方法
# metaclass是类的模板, 所以必须是'type'类型的派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value : self.append(value)
        return type.__new__(cls, name, bases, attrs)
class myList(list, metaclass=ListMetaclass):
    pass
# __new__方法接收的参数分别为:
#     1. 当前准备创建的类的对象
#     2. 类的名字
#     3. 类继承的父类集合
#     4. 类的方法集合
L = myList()
L.add(1)
print(L)





