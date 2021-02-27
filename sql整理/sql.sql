#student表增删改查,对于数字不管什么类型int或者varcharm，既可以加引号查询，也可以不加引号查询；
#增
//创建表格
CREATE TABLE student(
	id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,
	NAME VARCHAR(20)  CHARACTER SET utf8,
	age VARCHAR(5)
);
//添加多行数据
INSERT INTO student VALUES (1001,'张三',18),
(1002,'张四',20),
(1003,'张五',23),
(1004,'张六',24),
(1005,'江洋',25);
//在末尾添加一列
ALTER TABLE student ADD mobile INT(11);
//增加第一列
ALTER TABLE student ADD user_s INT(11) FIRST;

#删
//删除指定行
DELETE FROM student WHERE id=1005;
//删除指定列
ALTER TABLE student DROP mobile;
//清空指定表
DELETE FROM student; 
//清空指定表，执行效率高
TRUNCATE TABLE student;#truncate只能清空表，速度比delete块，但是不能一行一行删除；
//删除表格
DROP TABLE student;

#改
//修改指定列名
ALTER TABLE student CHANGE user_id id VARCHAR(10) CHARACTER SET utf8;
//修改任意指定内容
UPDATE student SET age=30 WHERE id=1001;
//修改指定表格名
RENAME TABLE teacher TO student;

#查
//查询指定整个表格
SELECT * FROM student;
//限制查询行数
SELECT * FROM student LIMIT 3;
//查询表格指定的列表
SELECT age FROM student;
//查询表格指定行
SELECT * FROM student WHERE id=1001;
//查询表格指定多行
SELECT * FROM student WHERE id IN (1001,1003,1005);
//模糊查询like
SELECT * FROM student WHERE NAME LIKE "%张%";
#----------------------------上面内容皆为单表操作；

//两表内连接
SELECT * FROM student JOIN grade ON student.`id`=grade.`id`;
//两表左连接
SELECT * FROM student LEFT JOIN grade ON student.`id`=grade.`id`;
//两表右连接
SELECT * FROM student RIGHT JOIN grade ON student.`id`=grade.`id`;
//两表选择指定列显示
SELECT student.`id`,student.`name`,student.`age`,grade.`kemu`,grade.`score` FROM student JOIN grade ON student.`id`=grade.`id`;
#----------------------------上面内容皆为多表操作
