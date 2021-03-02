create table Employee4 (
	id int,
	Company varchar,
	Salary int
);

insert into Employee4 values(1,'A',2341);
insert into Employee4 values(2,'A',341);
insert into Employee4 values(3,'A',15);
insert into Employee4 values(4,'A',15314);
insert into Employee4 values(5,'A',451);
insert into Employee4 values(6,'A',513);
insert into Employee4 values(7,'B',15);
insert into Employee4 values(8,'B',13);
insert into Employee4 values(9,'B',1154);
insert into Employee4 values(10,'B',1345);
insert into Employee4 values(11,'B',1221);
insert into Employee4 values(12,'B',234);
insert into Employee4 values(13,'C',2345);
insert into Employee4 values(14,'C',2645);
insert into Employee4 values(15,'C',2645);
insert into Employee4 values(16,'C',2652);
insert into Employee4 values(17,'C',65);

select id, company,salary
from(
  select id, company, salary, 
         row_number() over(partition by company order by salary) as      
         rno,
         count(*) over(partition by company) as cnt
  from Employee4) x
where rno in (ceil(cnt/2), cnt/2 + 1);
