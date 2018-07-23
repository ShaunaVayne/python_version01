#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# flask框架实现MVC渲染
from flask import Flask, render_template, request
from com.wk.WEB_APP_TEST.mysqlUtils import connectDB

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('home.html')

@app.route('/login',methods=['GET'])
def loginShow():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    userName = request.form['userName']
    passWord = request.form['passWord']
    flag = findUser(userName,passWord)
    if flag:
        return render_template('success.html',userName=userName)
    return render_template('login.html',message='login failed', userName=userName)

def findUser(userName, passWord):
    connect = connectDB('127.0.0.1', 3306, 'root', 'root123', 'wangkun')
    cursor = connect.cursor()
    cursor.execute('select * from user_test where user_name = %s and pass_word = %s',(userName,passWord,))
    fetchall = cursor.fetchall()
    size = fetchall.__len__()
    connect.close()
    if size == 1:
        return True
    return False

if __name__ == '__main__' :
    app.run()



