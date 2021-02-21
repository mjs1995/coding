create table Employee3 (
	Id int,
	Name varchar,
	Department varchar,
	ManagerID int
);

insert into Employee3 values(101,'John','A',null);
insert into Employee3 values(102,'Dan','A',101);
insert into Employee3 values(103,'James','A',101);
insert into Employee3 values(104,'Amy','A',101);
insert into Employee3 values(105,'Anne','A',101);
insert into Employee3 values(106,'Ron','B',101);

select name
from Employee3
where Id in 
	(select ManagerID 
	 from Employee3 
	 Group by ManagerID 
	 having count(*) > 4);
