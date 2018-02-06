# 定制类
class Student(object) :
    def __init__(self,name):
       self.name= name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

# print(Student('vayne'))

# __iter__ 函数
class Fib(object) :
    def __init__(self):
        self.a , self.b = 0, 1 #初始化两个计数器
    def __iter__(self):
        return self #返回自己
    def __next__(self):
        self.a , self.b = self.a + 1, self.b + 1
        if self.a > 1000:
            raise StopIteration()
        return self.a
for n in Fib():
    # print(n)
    pass

# __getitem__ 函数
class Fib1(object) :
    def __getitem__(self, item):
        a , b = 1, 1
        for x in range(item) :
            a, b = b, a + b
        return a
f = Fib1()
# print(f[100])

# __getattr__ 函数
class People(object) :
    def __init__(self):
        self.name = 'vayne'
    def __getattr__(self, item):
        if item == 'score' :
            return 989
p = People()
# print(p.score)

class Student1(object) :
    def __getattr__(self, item):
        if item == 'age' :
            return lambda : 25
s1 = Student1()
# print(s1.age())

# __call__ 函数 一个对象拥有自己的函数, 类似于java的构造函数
class Student2(object) :
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('my name is %s.' % self.name)
s2 = Student2('vayne')
s2()

