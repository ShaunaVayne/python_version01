# 连接mysql
import mysql.connector

connect = mysql.connector.connect(user='root', password='root123', database='wangkun')
# cursor = connect.cursor()
# # 创建user表
# cursor.execute('create table user (id VARCHAR(10) PRIMARY KEY , NAME  VARCHAR(20))')
# # 插入一行数据
# # 注意, 在python中mysql的占位符是%s, java中是?
# cursor.execute('insert into user(id, name) VALUES (%s , %s)',['1','WangKun'])
# # 操作影响的行数
# i = cursor.rowcount
# print(i)
# # 提交事物
# connect.commit()
# connect.close()

# 查询
connect_cursor = connect.cursor()
connect_cursor.execute('select * from user where id = %s',('1',))
fetchall = connect_cursor.fetchall()
print(fetchall)
connect.close()
