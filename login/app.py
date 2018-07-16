#coding:utf-8

from flask import Flask,request
import time
import random
import base64

app = Flask(__name__)

users = {
    "magigo":["123456"]
}

def gen_token(uid):
    token = base64.b64encode(':'.join([str(uid), str(random.random()), str(time.time() + 7200 )]))
    users[uid].append(token)
    return token

# 验证函数
def verify_token(token):
    _token = base64.b64decode(token)
    if not users.get(_token.split(':')[0])[-1] == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0

@app.route('/index', methods=['POST','GET'])
def index():
    print(request.headers)
    return 'hello'

@app.route('/login', methods=['POST','GET'])
def login():
    uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')
    if users.get(uid)[0] == pw:
        return gen_token(uid)
    else:
        return 'error'

# 用户登录测试
@app.route('/test', methods=['POST','GET'])
def test():
    token = request.args.get('token')
    if verify_token(token) == 1:
        return 'data'
    else:
        return 'error'

if __name__ == '__main__':
    app.run(debug=True)

