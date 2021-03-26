create table Sales1 (
 sale_date      date,    
 fruit          varchar,
 sold_num       int     
);

insert into Sales1 values('2020-05-01','apples',10);
insert into Sales1 values('2020-05-01','oranges',8);
insert into Sales1 values('2020-05-02','apples',15);
insert into Sales1 values('2020-05-02','oranges',15);
insert into Sales1 values('2020-05-03','apples',20);
insert into Sales1 values('2020-05-03','oranges',0);
insert into Sales1 values('2020-05-04','apples',15);
insert into Sales1 values('2020-05-04','oranges',16);

select sale_date, sum(case when fruit = 'apples' then sold_num else - sold_num end) as diff
from Sales1
group by sale_date
order by sale_date
