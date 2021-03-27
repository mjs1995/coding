create table Employees_1 (
 employee_id    int,     
 employee_name  varchar,
 manager_id     int     
);

insert into Employees_1 values(1,'Boss',1);
insert into Employees_1 values(3,'Alice',3);
insert into Employees_1 values(2,'Bob',1);
insert into Employees_1 values(4,'Daniel',2);
insert into Employees_1 values(7,'Luis',4);
insert into Employees_1 values(8,'Jhon',3);
insert into Employees_1 values(9,'Angela',8);
insert into Employees_1 values(77,'Robert',1);

select t1.employee_id
from Employees_1 t1 
inner join Employees_1 as t2 on t1.manager_id = t2.employee_id
join Employees_1 t3 on t2.manager_id = t3.employee_id
where t3.manager_id = 1 and t1.employee_id != 1

select employee_id as EMPLOYEE_ID from Employees_1 where manager_id in
(select employee_id from Employees_1 WHERE manager_id in
(select employee_id from Employees_1 where manager_id =1))
and employee_id !=1
