create table Departments(
	id int,
	name varchar
);

create table Students(
	id int,
	name varchar,
	department_id int
);

insert into Departments values(1,'Electrical Engineering');
insert into Departments values(7,'Computer Engineering');
insert into Departments values(13,'Bussiness Administration');

insert into Students values(23,'Alice',1);
insert into Students values(1,'Bob',7);
insert into Students values(5,'Jennifer',13);
insert into Students values(2,'John',14);
insert into Students values(4,'Jasmine',77);
insert into Students values(3,'Steve',74);
insert into Students values(6,'Luis',1);
insert into Students values(8,'Jonathan',7);
insert into Students values(7,'Daiana',33);
insert into Students values(11,'Madelynn',1);

select id, name
from Students
where department_id not in (select id
							from Departments)
