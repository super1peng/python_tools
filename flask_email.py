#coding:utf-8

import os  
from flask import Flask  
from flask_mail import Mail  
from flask_script import Manager  
app = Flask(__name__)  
manager = Manager(app)  
  
app.config['MAIL_SERVER'] = 'smtp.qq.com'  
app.config['MAIL_PORT'] = 25  
app.config['MAIL_USE_TLS'] = True  
app.config['MAIL_PASSWORD'] = '授权码'  
app.config['MAIL_USERNAME'] = '发送者邮箱'  
  
mail = Mail(app)  
  
if __name__ == '__main__':  
    manager.run()  
    #app.run()  