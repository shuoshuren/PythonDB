#! /usr/bin/python
# coding:utf-8

from pymysql import *

"""
sql语句参数化

"""


def insert(name):
    try:
        conn = connect(host='localhost', port=3306, db='python3', user='root', passwd='mysql', charset='utf8')
        cursor1 = conn.cursor()

        sql = 'insert into students(name) values(%s)'
        cursor1.execute(sql,args=[name])
        conn.commit()

        cursor1.close()
        conn.close()
        print("ok")
    except Exception:
        print(Exception)


if __name__ == '__main__':
    name = input("请输入用户名：")
    insert(name)
