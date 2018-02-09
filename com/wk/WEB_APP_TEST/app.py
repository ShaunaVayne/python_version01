#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-
'''
    编码一个app.py,处理三个url,分别为:
    GET /:首页,返回Home;
    GET /signin:登录页,显示登录表单;
    POST /signin:处理登录表单,显示登录结果
'''
from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'
@app.route('/signin', methods=['GET'])
def signin_form():
    return '''
            <form action='/signin' method='post'>
                <table>
                    <tr><td>username:</td><td><input type='text' name='username'/></td></tr>
                    <tr><td>password:</td><td><input type='password' name='password'/></td></tr>
                    <tr><td></td><td><button>sign in</button></td></tr>
                </table>
            </form>
            '''
@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request域中读取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
        return '<h3 style="color: green">hello %s!</h3>'%(request.form['username'])
    return '<h3 style="color:red">login failed</h3>'
if __name__ == '__main__':
    app.run()