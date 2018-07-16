#coding:utf-8

import requests

# r =requests.get('http://127.0.0.1:5000/login', auth=('magigo','123456'))
#
# print(r.text)


# 请求数据部分
token = 'bWFnaWdvOjAuOTQwMzI0NDYyNzI5OjE1MzE3MzE3NTUuMjg='
r = requests.get('http://127.0.0.1:5000/test',params={'token':token })
print(r.text)