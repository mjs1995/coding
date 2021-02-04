create table Logs (
	log_id int
);

insert into Logs values(1);
insert into Logs values(2);
insert into Logs values(3);
insert into Logs values(7);
insert into Logs values(8);
insert into Logs values(10);

select log_start.log_id as START_ID, min(log_end.log_id) as END_ID
from 
	(select log_id from Logs where log_id - 1 not in (select * from Logs)) as log_start,
	(select log_id from Logs where log_id + 1 not in (select * from Logs)) as log_end
where log_start.log_id <= log_end.log_id
group by log_start.log_id
order by log_start.log_id;
