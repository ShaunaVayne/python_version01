# 定义其他类型的Field : StringField
from com.wk.test5.orm.Field import Field


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

