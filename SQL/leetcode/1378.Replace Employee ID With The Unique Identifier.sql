create table Employees (
	id int,
	name varchar
);

create table EmployeeUNI (
	id int,
	unique_id int
);

insert into Employees values(1, 'Alice');
insert into Employees values(7, 'Bob');
insert into Employees values(11, 'Meir');
insert into Employees values(90, 'Winston');
insert into Employees values(3, 'Jonathan');

insert into EmployeeUNI values(3,1);
insert into EmployeeUNI values(11,2);
insert into EmployeeUNI values(90,3);

select unique_id, name
from Employees as a
left join EmployeeUNI as b on a.id = b.id;
