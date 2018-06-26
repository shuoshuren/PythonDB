# PythonDB
## 交互类型
### Connection对象
> 调用connect()方法，用于建立于数据库的连接
>`conn = connect(参数列表)`
+ host:连接的mysql主机，如果是本机是'localhost'
+ port:连接的mysql主机端口，默认是3306
+ db:数据库的名称
+ user:连接的用户名
+ password：连接的密码
+ charset :通信采用的编码方式,推荐utf8
> 对象方法
+ close() 关闭连接
+ commit()事务，提交后生效
+ rollback() 事务，放弃之前打操作
+ cursor()返回Cursor对象，用于执行sql语句并获得结果

### Cursor对象
> 调用Connection对象打cursor()方法创建对象
>`cursor1 = conn.cursor()`
> 对象方法
+ close() 关闭
+ execute(operation \[,parameter])执行语句，返回影响的行数
+ fetchone() 执行查询语句，获取查询结果集的第一个行数据返回一个元组
+ next()执行查询语句时，获取当前行打下一行
+ fetchall() 执行查询时，获取查询结果集的所有行，一行构成一个元组，再将元组转入一个元组中返回
+ scoll(value\[,mode])将指针移动到某个位置
    + mode表示移动方式
    + mode的默认值为relative,表示基于当前行移动到value，value为正表示向下移动，value为负表示向上移动
    + mode的值为absolute，表示基于第一条数据的位置，第一条数据的位置为0






