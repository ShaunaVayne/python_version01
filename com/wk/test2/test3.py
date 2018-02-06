# -*- coding: UTF-8 -*-
# py -v(2)
class OldClass :
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

#py -v(3)
class NewClass(object) :
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

if __name__ == '__main__' :
    old_class = OldClass('wangkun',22);
    print(old_class)
    print(type(old_class))
    print(dir(old_class))
    print(old_class.__dict__)
    print("\n")
    new_class = NewClass('liujia',21);
    print(new_class)
    print(type(new_class))
    print(dir(new_class))
    print(new_class.__dict__)
