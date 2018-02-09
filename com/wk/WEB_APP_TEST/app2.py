#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
# flask框架实现MVC渲染
import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('home.html')
@app.route('/login',methods=['GET'])
def loginShow():
    return render_template('login.html')

def findUser(userName, passWord):
    connect = mysql.connector.connect(user='root', password='root123', database='wangkun')
    cursor = connect.cursor()
    cursor.execute('select * from user_test where user_name = %s and pass_word = %s',(userName,passWord,))
    fetchall = cursor.fetchall()
    size = fetchall.__len__()
    connect.close()
    if size == 1:
        return True
    return False

@app.route('/login',methods=['POST'])
def login():
    userName = request.form['userName']
    passWord = request.form['passWord']
    flag = findUser(userName,passWord)
    if flag:
        return render_template('success.html',userName=userName)
    return render_template('login.html',message='login failed', userName=userName)

if __name__ == '__main__' :
    app.run()



