create table Events(
 business_id    int     ,
 event_type     varchar ,
 occurences     int     
);

insert into Events values(1,'reviews',7);
insert into Events values(3,'reviews',3);
insert into Events values(1,'ads',11);
insert into Events values(2,'ads',7);
insert into Events values(3,'ads',6);
insert into Events values(1,'page review',3);
insert into Events values(2,'page review',12);

select a.business_id
from (
	select business_id, event_type, avg(occurences) as avgo
	from Events
	group by business_id, event_type) as a inner join
	(select event_type, avg(occurences) as avgo
	 from Events
	 group by event_type) as b 
on a.event_type = b.event_type
where a.avgo > b.avgo
group by business_id
having count(1) >1
