#coding:utf-8

from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@manager.command
def hello():
	print("hello, world!")

@manager.option('-m', '--msg', dest='msg_val', default="word")
def hello_world(msg_val):
	print("hello" + msg_val)

if __name__ == '__main__':
	manager.run()
	