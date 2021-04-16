CREATE TABLE Activity1 (
	player_id int,
	device_id int,
	event_date date,
	games_played int
	);
	
INSERT INTO Activity1 VALUES ( 1, 2,'2016/03/01',5 );
INSERT INTO Activity1 VALUES ( 1, 2,'2016/03/02',6 );
INSERT INTO Activity1 VALUES ( 2, 3,'2017/06/25' ,1 );
INSERT INTO Activity1 VALUES ( 3, 1,'2016/03/02',0 );
INSERT INTO Activity1 VALUES ( 3, 4,'2018/07/03',5 );

with players as 
(
select 
	case
		when datediff(day, end_date, event_date) = 1 then player_id
	end as player
from
(select *, lag(event_date,1) over (order by event_date) as end_date from Activity1) t)
select round(count(player) / cast((select count(distinct player_id) from activity) as float), 2) as fraction
from Players 
where player is not null
