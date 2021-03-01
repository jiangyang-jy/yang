#//创建学生表，且插入数据
CREATE TABLE student(
	Sid VARCHAR(10),
	Sname VARCHAR(20) CHARACTER SET utf8,
	Sage INT(5)
);
INSERT INTO student VALUES('s01','唐妍',18),
('s02','胡哥',19),
('s03','刘诗',18),
('s04','杨蜜',17),
('s05','何建华',19),
('s06','彭鱼彦',18);
SELECT * FROM student;

#//创建教师表，且插入数据
CREATE TABLE teacher(
	Tid VARCHAR(10),
	Tname VARCHAR(20) CHARACTER SET utf8
);
INSERT INTO teacher VALUES('t01','高磊'),
('t02','韩争'),
('t03','李征辉'),
('t04','何倩文'),
('t05','刘宏'),
('t06','彭伟');
SELECT * FROM teacher;

#//创建班级表，且插入数据
CREATE TABLE class(
	Cid VARCHAR(10),
	Cname VARCHAR(20) CHARACTER SET utf8,
	Cteacher VARCHAR(10) CHARACTER SET utf8
);
INSERT INTO class VALUES ('c01','高等数学','高磊'),
('c02','英语','韩争'),
('c03','计算机基础','李征辉'),
('c04','汇编语言','何倩文'),
('c05','电子商务','李征辉');
SELECT * FROM class;

#//创建成绩表，且插入数据
CREATE TABLE grade(
	Sid VARCHAR(10),
	Cid VARCHAR(10),
	Cscore INT(3)
);
INSERT INTO grade VALUES('s01','c01',58),
('s01','c02',59),
('s01','c03',55),
('s02','c02',83),
('s02','c05',79),
('s02','c04',77),
('s03','c01',55),
('s03','c03',81),
('s03','c04',73),
('s04','c01',67),
('s04','c02',78),
('s04','c03',82),
('s04','c05',80),
('s05','c01',61),
('s04','c04',78);
SELECT * FROM grade;

//查询名字中含有"华"字的学生信息
SELECT * FROM student WHERE Sname LIKE "%华%";
//查询并统计同龄学生人数
SELECT sage,COUNT(Sid) FROM student GROUP BY sage;
//查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列
SELECT Cid,AVG(Cscore) FROM grade GROUP BY Cid ORDER BY AVG(Cscore),cid DESC;
//按平均成绩从高到低显示所有学生的平均成绩
SELECT Sid,AVG(Cscore) FROM grade GROUP BY Sid ORDER BY AVG(Cscore) DESC;
//按各科平均成绩从低到高顺序排序
SELECT Cid,AVG(Cscore) FROM grade GROUP BY Cid ORDER BY AVG(Cscore) ASC;