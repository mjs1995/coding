create table Activity_1(
 user_id        int,     
 session_id     int,     
 activity_date  date,    
 activity_type  varchar    
);

insert into Activity_1 values(1,1,'2019-07-20','open_session');
insert into Activity_1 values(1,1,'2019-07-20','scroll_down');
insert into Activity_1 values(1,1,'2019-07-20','end_session');
insert into Activity_1 values(2,4,'2019-07-20','open_session');
insert into Activity_1 values(2,4,'2019-07-21','send_message');
insert into Activity_1 values(2,4,'2019-07-21','end_session');
insert into Activity_1 values(3,2,'2019-07-21','open_session');
insert into Activity_1 values(3,2,'2019-07-21','send_message');
insert into Activity_1 values(3,2,'2019-07-21','end_session');
insert into Activity_1 values(4,3,'2019-06-25','open_session');
insert into Activity_1 values(4,3,'2019-06-25','end_session');

select activity_date as day, count(distinct user_id) as active_users
from Activity_1
where activity_date between '2019-06-28' and '2019-07-27'
group by activity_date
