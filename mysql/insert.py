#! /usr/bin/python
# coding:utf-8

from pymysql import *

"""
向mysql数据库中插入数据

"""


def insert():
    try:
        conn = connect(host='localhost', port=3306, db='python3', user='root', passwd='mysql', charset='utf8')
        cursor1 = conn.cursor()

        sql = 'insert into students(name) values("郭小二")'
        cursor1.execute(sql)
        conn.commit()

        cursor1.close()
        conn.close()
    except Exception:
        print(Exception)


if __name__ == '__main__':
    insert()
