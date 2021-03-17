create table cinema (
	seat_id int,
	free int
);

insert into cinema values(1,1);
insert into cinema values(2,0);
insert into cinema values(3,1);
insert into cinema values(4,1);
insert into cinema values(5,1);

select distinct c1.seat_id
from cinema as c1, cinema as c2
where c1.free = 1 and c2.free = 1 and (c2.seat_id = c1.seat_id + 1 or c2.seat_id = c1.seat_id - 1)
order by seat_id
