create table Customers_1(
 customer_id    int,     
 name           varchar 
);

create table orders_1(
 order_id       int     ,
 order_date     date    ,
 customer_id    int     ,
 cost           int     
);

insert into Customers_1 values(1,'Winston');
insert into Customers_1 values(2,'Jonathan');
insert into Customers_1 values(3,'Annabelle');
insert into Customers_1 values(4,'Marwan');
insert into Customers_1 values(5,'Khaled');

insert into orders_1 values(1,'2020-07-31',1,30);
insert into orders_1 values(2,'2020-07-30',2,40);
insert into orders_1 values(3,'2020-07-31',3,70);
insert into orders_1 values(4,'2020-07-29',4,100);
insert into orders_1 values(5,'2020-06-10',1,1010);
insert into orders_1 values(6,'2020-08-01',2,102);
insert into orders_1 values(7,'2020-08-01',3,111);
insert into orders_1 values(8,'2020-08-03',1,99);
insert into orders_1 values(9,'2020-08-07',2,32);
insert into orders_1 values(10,'2020-07-15',1,2);

select a.name as customer_name, a.customer_id, b.order_id
from Customers_1 a join orders_1 b on a.customer_id = b.customer_id
where (
	select count(*)
	from orders_1 as b2
	where b.customer_id = b2.customer_id and b.order_date < b2.order_date) <= 2
order by a.name,a.customer_id, b.order_date desc
