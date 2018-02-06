# 1.将对象转成json串
import json

d = dict(name = 'wangkun', age = 22)
j = json.dumps(d)
print(j)

# 2.将json反序列化成对象
json_str = '{"name" : "wangkun2","age" : 22}'
obj = json.loads(json_str)
print(obj)

# 3.进阶,class与json的序列化
class Student(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age
s = Student(name = 'wangmingming', age = 22)
student = json.dumps(s)
print(student)
# 若只是json.dumps(s)这样写会抛异常,Student类不能被json序列化,因为在默认情况下,
# dumps函数并不知道将实例转换成一个json对象,需要在方法参数里加上一个转换函数, 如下:
def StudentDict(s) :
    return {
        'name' : s.name,
        'age' : s.age
    }
class Student(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age
s = Student(name = 'wangmingming', age = 22)
student = json.dumps(s, default = StudentDict)
# 但是如果遇到比如说Teacher, 同样不能被序列化, 可以直接把类变成dict才是最解耦的写法, 如下:
s2 = Student(name = 'xiaoming', age = 23)
print(json.dumps(s2, default= lambda a : a.__dict__))
print(student)

# 将json反序列为对象 object_hook函数负责将dict转换成实例
def dictToObject(d):
    return Student(d['name'],d['age'])
json_str2 = '{"name": "xiaoming", "age": 23}'
print(json.loads(json_str2, object_hook= dictToObject))
