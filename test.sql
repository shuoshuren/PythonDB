
# 创建表

create table static_info(
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	content varchar(50) not null,
	count int not null,
	year int not null,
	month int not null,
	day int not null,
	time varchar(50) not null
);

# 插入数据
insert into static_info values(null,"第一天数据",7,2018,12,9,"05:32:32");
insert into static_info values(null,"第二条数据",7,2018,12,8,"05:32:32");
insert into static_info values(null,"第一天数据",7,2019,1,9,"05:32:32");
insert into static_info values(null,"第二天数据",7,2019,1,9,"05:32:32");
insert into static_info values(null,"第一天数据",7,2019,1,8,"05:32:32");
insert into static_info values(null,"第二天数据",7,2018,11,9,"05:32:32");
insert into static_info values(null,"第一天数据",7,2019,2,9,"05:32:32");
insert into static_info values(null,"第二天数据",7,2018,11,23,"05:32:32");
insert into static_info values(null,"第二天数据",7,2018,12,10,"05:32:32");
insert into static_info values(null,"第一天数据",7,2019,1,7,"05:32:32");
insert into static_info values(null,"第二天数据",7,2019,1,7,"05:32:32");
insert into static_info values(null,"第三天数据",7,2019,1,7,"05:32:32");
insert into static_info values(null,"第一天数据",7,2019,1,7,"05:32:32");
insert into static_info values(null,"第二天数据",7,2019,1,7,"06:32:32");
insert into static_info values(null,"第三天数据",7,2019,1,7,"05:32:32");
insert into static_info values(null,"第一天数据",7,2019,1,9,"05:32:32");


# 查询有多少日期
select year,month,day from static_info group by year,month,day order by year,month,day;

# 查询有多少月
select year,month from static_info group by year,month order by year,month;

# 查询有多少年
select year from static_info group by year order by year;

# 查询某天的数据
select *,sum(count) from static_info where year=2019 and month=1 and day=7 group by content,time order by time;

# 查询某一月的数据
select *,sum(count) from static_info where year=2019 and month=1 group by content,day order by day;

# 查询某一年的数据
select *,sum(count) from static_info where year=2019 group by content,month,day order by month,day;