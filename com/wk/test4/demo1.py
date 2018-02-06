#   面向对象
class student(object) :
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def introduce(self) :
        print('%s %s' % (self.__name, self.__age))

stu1 = student('wangkun',22)
stu1.set_name('wangminming')
print(stu1.get_name())
stu1.introduce()