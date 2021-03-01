create table follow1 (
	followee varchar,
	follower varchar
);

insert into follow1 values('A','B');
insert into follow1 values('B','C');
insert into follow1 values('B','D');
insert into follow1 values('D','E');

select a.followee as follower,
	COUNT(distinct a.follower) as num
from follow1 a join follow1 b on a.followee=b.follower
group by a.followee
