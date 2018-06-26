#! /usr/bin/python
# coding:utf-8

from pymysql import *

"""
向mysql数据库中更改数据

"""


def update():
    """更新数据"""
    try:
        conn = connect(host='localhost', port=3306, db='python3', user='root', passwd='mysql', charset='utf8')
        cursor1 = conn.cursor()

        sql = 'update students set name = "王二小" where id = 8'
        cursor1.execute(sql)
        conn.commit()

        cursor1.close()
        conn.close()
        print("ok")
    except Exception:
        print(Exception)


def delete():
    """删除数据"""
    try:
        conn = connect(host='localhost', port=3306, db='python3', user='root', passwd='mysql', charset='utf8')
        cursor1 = conn.cursor()

        sql = 'delete from students where id = 8'
        cursor1.execute(sql)
        conn.commit()

        cursor1.close()
        conn.close()
        print("ok")
    except Exception:
        print(Exception)


if __name__ == '__main__':
    delete()
