create table Product_1 (
	product_id int,
	product_name varchar,
	unit_price int
);

create table Sales_1 (
	seller_id   int,
	product_id int,
	buyer_id int,
	sale_date  date,
	quantity int,
	price int
);

insert into Product_1 values(1,'S8',1000);
insert into Product_1 values(2,'G4',800);
insert into Product_1 values(3,'iPhone',1400);

insert into Sales_1 values(1,1,1,'2019-01-21',2,2000);
insert into Sales_1 values(1,2,2,'2019-02-17',1,800);
insert into Sales_1 values(2,2,3,'2019-06-02',1,800);
insert into Sales_1 values(3,3,4,'2019-05-13',2,2800);


select seller_id
from Sales_1
group by seller_id
having sum(price) = (select sum(price)
					 from Sales_1
					 group by seller_id
					 order by sum(price) DESC
					 limit 1)
order by seller_id
