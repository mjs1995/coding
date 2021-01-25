create table Employee_t (
	id int,
	month int,
	salary int
);

insert into Employee_t values (1, 1, 20);
insert into Employee_t values (2, 1, 20);
insert into Employee_t values (1, 2, 30);
insert into Employee_t values (2, 2, 30);
insert into Employee_t values (3, 2, 40);
insert into Employee_t values (1, 3, 40);
insert into Employee_t values (3, 3, 60);
insert into Employee_t values (1, 4, 60);
insert into Employee_t values (3, 4, 70);

select
	a.id,
	a.month,
	sum(b.salary) salay
from
	Employee_t a join Employee_t b on
	a.id = b.id and
	a.month - b.month >= 0 and
	a.month - b.month < 3
group by
	a.id, a.month
having 
	(a.id, a.month) not in (select id, max(month) from Employee_t group by id)
order by
	a.id, a.month Desc
