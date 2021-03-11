create table orders4 (
	order_number 	int,
	customer_number	int,
	order_date	date,
	required_date	date,
	shipped_date	date,
	status	char(15),
	comment	char(200)
);

insert into orders4 values(1,1,'2017-04-09','2017-04-13','2017-04-12','Closed','');
insert into orders4 values(2,2,'2017-04-15','2017-04-20','2017-04-18','Closed','');
insert into orders4 values(3,3,'2017-04-16','2017-04-25','2017-04-20','Closed','');
insert into orders4 values(4,3,'2017-04-18','2017-04-28','2017-04-25','Closed','');

select customer_number 
from orders4
group by customer_number
order by count(*) DESC LIMIT 1;
