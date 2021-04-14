create table student(
student_id int,
student_name varchar(10),
gender varchar(2),
dept_id int
);
 
insert into student values(1,'Jack','M',1);
insert into student values(2,'Jane','F',1);
insert into student values(3,'Mark','M',2);
 
select * from student
 
create table department
(
dept_id int,
dept_name varchar(25)
);
 
insert into department values(1,'Engineering');
insert into department values(2,'Science');
insert into department values(3,'Law');
 
select * from department;

select d.dept_name, count(s.student_id) as student_number 
from department d left join student s on d.dept_id = s.dept_id 
group by d.dept_name
order by student_number desc
