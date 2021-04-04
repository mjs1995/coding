create table Queue(
 person_id    int     ,
 person_name  varchar ,
 weight       int     ,
 turn         int     
);

insert into Queue values(5,'George Washington',250,1);
insert into Queue values(3,'John Adams',350,2);
insert into Queue values(6,'Thomas Jefferson',400,3);
insert into Queue values(2,'Will Johnliams',200,4);
insert into Queue values(4,'Thomas Jefferson',175,5);
insert into Queue values(1,'James Elephant',500,6);

select person_name
from Queue a 
where (select sum(weight)
	   from Queue
	   where a.turn >= turn) <= 1000
order by a.turn desc limit 1
