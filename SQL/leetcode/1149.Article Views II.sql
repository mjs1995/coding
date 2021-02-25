create table Views1 (
 article_id     int,     
 author_id      int,     
 viewer_id      int,     
 view_date      date    
);

insert into Views1 Values(1,3,5,'2019-08-01');
insert into Views1 Values(3,4,5,'2019-08-01');
insert into Views1 Values(1,3,6,'2019-08-02');
insert into Views1 Values(2,7,7,'2019-08-01');
insert into Views1 Values(2,7,6,'2019-08-02');
insert into Views1 Values(4,7,1,'2019-07-22');
insert into Views1 Values(3,4,4,'2019-07-21');
insert into Views1 Values(3,4,4,'2019-07-21');

select distinct viewer_id as id
from Views1
group by viewer_id, view_date
having count(distinct article_id) > 1;
