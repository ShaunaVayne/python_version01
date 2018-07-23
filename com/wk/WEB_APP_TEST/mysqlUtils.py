#/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: WangKun
# @Date: Created in 2018/7/23 上午11:51
# @Version: 1.0.0
# @Description:
import pymysql.cursors

def connectDB(url,port,uname,pwd,database):
    connection = pymysql.connect(host=url, port=port, user=uname, password=pwd, db=database, charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    return connection
