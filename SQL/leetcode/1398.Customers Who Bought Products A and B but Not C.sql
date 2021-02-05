create table Customers (
	customer_id int,  
	customer_name varchar
);

create table Orders (
	 order_id       int,     
	 customer_id    int,     
	 product_name   varchar 

)

insert into Customers values(1, 'Daniel');
insert into Customers values(2, 'Diana');
insert into Customers values(3, 'Elizabeth');
insert into Customers values(4, 'Jhon');

insert into Orders values(10,1,'A');
insert into Orders values(20,1,'B');
insert into Orders values(30,1,'D');
insert into Orders values(40,1,'C');
insert into Orders values(50,2,'A');
insert into Orders values(60,3,'A');
insert into Orders values(70,3,'B');
insert into Orders values(80,3,'D');
insert into Orders values(90,4,'C');

select *
from Customers
where customer_id in
	(select distinct customer_id
	 from Orders
	 where product_name = 'A'
		and customer_id in
			(select distinct customer_id
			from Orders
			where product_name = 'B')
			and customer_id not in
				(select distinct customer_id
				from Orders
				where product_name = 'C'))
