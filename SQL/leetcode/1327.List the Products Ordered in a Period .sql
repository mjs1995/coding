create table Products1 (
	 product_id        int,
	 product_name      varchar, 
	 product_category  varchar 
);

create table Orders1 (
	 product_id     int,   
	 order_date     date,   
	 unit           int     
);

insert into Products1 values(1,'Leetcode Solutions','Book');
insert into Products1 values(2,'Jewels of Stringology','Book');
insert into Products1 values(3,'HP','Laptop');
insert into Products1 values(4,'Lenovo','Laptop');
insert into Products1 values(5,'Leetcode Kit','T-shirt');

insert into Orders1 values(1, '2020-02-05',60);
insert into Orders1 values(1, '2020-02-10',70);
insert into Orders1 values(2, '2020-01-18',30);
insert into Orders1 values(2, '2020-02-11',80);
insert into Orders1 values(3, '2020-02-17',2);
insert into Orders1 values(3, '2020-02-24',3);
insert into Orders1 values(4, '2020-03-01',20);
insert into Orders1 values(4, '2020-03-04',30);
insert into Orders1 values(4, '2020-03-04',60);
insert into Orders1 values(5, '2020-02-25',50);
insert into Orders1 values(5, '2020-02-07',50);
insert into Orders1 values(5, '2020-03-01',50);

select a.product_name, sum(unit) as unit
from Products1 a inner join Orders1 b on a.product_id = b.product_id
where Left(b.order_date,7) = "2020-02"
group by a.product_name
having sum(unit) >100
