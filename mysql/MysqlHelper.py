#!/usr/bin/python
# coding:utf-8
from pymysql import *


class MysqlHelper(object):
    """
    mysql操作封装

    """

    def __init__(self, host, port, db, user, password, charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host, port=self.port, db=self.db, user=self.user, password=self.password,
                            charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def cud(self, sql, params):
        try:
            self.open()

            self.cursor.execute(sql, params)
            self.conn.commit()

            self.close()
        except Exception:
            print(Exception)

    def all(self, sql, params=[]):
        # try:
        self.open()
        self.cursor.execute(sql, params)
        result = self.cursor.fetchall()
        self.close()
        return result
    # except Exception:
    #     print(Exception)


def test_cud():
    name = input("请输入学生姓名：")
    userId = input("请输入学生编号：")
    sql = 'update students set name=%s where id=$s '
    params = [name, userId]

    sqlHelper = MysqlHelper('localhost', 3306, 'python3', 'root', 'mysql')
    sqlHelper.cud(sql, params)


def test_query():
    sql = 'select id,name from students where id<5'
    sqlHelper = MysqlHelper('localhost', 3306, 'python3', 'root', 'mysql')
    result = sqlHelper.all(sql)
    print(result)


if __name__ == '__main__':
    test_query()
