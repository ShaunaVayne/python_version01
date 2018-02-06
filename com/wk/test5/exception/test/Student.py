# 对Student类进行测试
class Student(object) :
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score > 100 or self.score < 0 :
            raise ValueError('params is not available')
        if self.score >= 60 and self.score < 80 :
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'
