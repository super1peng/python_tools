#coding:utf-8


import os
import subprocess


def shell():
	# (status, output) = commands.getstatusoutput('ls /bin/ls') 
	# print(status, output)
	# os.system("python3 flask_email.py shell")

	p = subprocess.Popen('python3 flask_email.py shell',shell=True,stdin=subprocess.PIPE)

	
	p.stdin.write(b'from flask_mail import Message \n')
	p.stdin.write(b"from flask_email import mail  \n")
	p.stdin.write(b"msg = Message('test subject', sender='发送者邮箱', recipients=['接收者邮箱'])\n")
	p.stdin.write(b"msg.body = 'text body'\n")
	p.stdin.write(b"msg.html = '<b>HTML</b> body'\n")
	p.stdin.write(b"with app.app_context():\n")
	p.stdin.write(b"    mail.send(msg)\n")
	p.stdin.write(b"\n")
	p.stdin.write(b"\n")

def main():
	shell()

if __name__ == '__main__':
	main()