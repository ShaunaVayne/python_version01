# 定义其他类型的Field : IntegerField
from com.wk.test5.orm.Field import Field


class IntegerField(Field) :
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
