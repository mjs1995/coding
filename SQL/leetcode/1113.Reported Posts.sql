create table Actions (
 user_id        int,     
 post_id        int,     
 action_date    date,     
 action         varchar,    
 extra          varchar
);

insert into Actions values(1,1,'2019-07-01','view','null');
insert into Actions values(1,1,'2019-07-01','like','null');
insert into Actions values(1,1,'2019-07-01','share','null');
insert into Actions values(2,4,'2019-07-04','view','null');
insert into Actions values(2,4,'2019-07-04','report','spam');
insert into Actions values(3,4,'2019-07-04','view','null');
insert into Actions values(3,4,'2019-07-04','report','sapm');
insert into Actions values(4,3,'2019-07-02','view','null');
insert into Actions values(4,3,'2019-07-02','report','spam');
insert into Actions values(5,2,'2019-07-04','view','null');
insert into Actions values(5,2,'2019-07-04','report','racism');
insert into Actions values(5,5,'2019-07-04','view','null');
insert into Actions values(5,5,'2019-07-04','report','racism');

select extra as report_reason, count(distinct post_id) as report_count
from Actions
where action_date = '2019-07-04' and action = 'report'
group by extra
