# 测试类
from com.wk.test5.orm.IntegerField import IntegerField
from com.wk.test5.orm.Model import Model
from com.wk.test5.orm.StringField import StringField


class User(Model) :
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例
u = User(id=12, name='wangkun', email = 'ahaqwjwk@163.com', password ='095430')
u.save();