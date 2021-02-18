create table Customer (
	customer_id int,
	product_key int
);

create table Product1 (
	product_key int
);

insert into Customer values(1,5);
insert into Customer values(2,6);
insert into Customer values(3,5);
insert into Customer values(3,6);
insert into Customer values(1,6);

insert into Product1 values(5);
insert into Product1 values(6);

select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (
	select count(1) from Product1)
