create table Delivery (
	delivery_id int,
	customer_id int,
	order_date date,
	customer_pref_delivery_date date
);

insert into Delivery values(1,1,'2019-08-01','2019-08-02');
insert into Delivery values(2,5,'2019-08-02','2019-08-02');
insert into Delivery values(3,1,'2019-08-11','2019-08-11');
insert into Delivery values(4,3,'2019-08-24','2019-08-26');
insert into Delivery values(5,4,'2019-08-21','2019-08-22');
insert into Delivery values(6,2,'2019-08-11','2019-08-13');

select round(100*sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)/count(1),2) immediate_percentage 
from Delivery
