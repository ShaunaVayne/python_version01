class Student(object):
    __slots__ = ('name', 'age')
s = Student()
s.name = 'adle'
s.age = 20
s.score = 90
print(s.score)
