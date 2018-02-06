#   继承多态
class Animal(object):
    def run(self):
        print('Animal is running')

class dog(Animal):
    def run(self):
        print('dog is running')
d = dog()
# d.run()

class cat(Animal):
    def run(self):
        print('cat is running')
c = cat()
def run_twice(Animal):
    Animal.run()

# run_twice(d)
# run_twice(c)

def fn() :
    pass
# print(type(fn) == types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
# print(type(lambda x : x+1) == types.LambdaType)


class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x **2

obj = MyObject()

print(hasattr(obj,'x'))
setattr(obj,'y',19)
print(getattr(obj,'y'))
print(obj.y)

fn = getattr(obj,'power')
print(fn())


class people(object):
    name = 'wangkun'
p = people()
print(p.name)
print(people.name)
p.name = 'wangmingming'
print(p.name)
print(people.name)
del p.name
print(p.name)



