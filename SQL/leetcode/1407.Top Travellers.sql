create table Users1 (
	id int,
	name varchar
);

create table Rides (
	id int,
	user_id int,
	distance int
);

insert into Users1 values (1, 'Alice');
insert into Users1 values (2, 'Bob');
insert into Users1 values (3, 'Alex');
insert into Users1 values (4, 'Donald');
insert into Users1 values (7, 'Lee');
insert into Users1 values (13, 'Jonathan');
insert into Users1 values (19, 'Elvis');

insert into Rides values (1,1,120);
insert into Rides values (2,2,317);
insert into Rides values (3,3,222);
insert into Rides values (4,7,100);
insert into Rides values (5,13,312);
insert into Rides values (6,19,50);
insert into Rides values (7,7,120);
insert into Rides values (8,19,400);
insert into Rides values (9,7,230);

select a.name, coalesce(sum(b.distance),0) as travelled_distance
from Users1 a left join Rides b on a.id = b.user_id
group by a.id, a.name
order by travelled_distance desc
