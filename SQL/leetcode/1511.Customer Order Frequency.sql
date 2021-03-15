create table Customers_2 (
 customer_id    int,     
 name           varchar, 
 country        varchar 
);

create table Product_2 (
 product_id     int,     
 description    varchar, 
 price          int     
);

create table Orders_2 (
 order_id       int,     
 customer_id    int,     
 product_id     int,     
 order_date     date,    
 quantity       int     
);

insert into Customers_2 values(1,'Winston','USA');
insert into Customers_2 values(2,'Jonathan','Peru');
insert into Customers_2 values(3,'Moustafa','Egypt');

insert into Product_2 values(10,'LC Phone','300');
insert into Product_2 values(20,'LC T-Shirt','10');
insert into Product_2 values(30,'LC Book','45');
insert into Product_2 values(40,'LC Keychain','2');

insert into Orders_2 values(1,1,10,'2020-06-10',1);
insert into Orders_2 values(2,1,20,'2020-07-01',1);
insert into Orders_2 values(3,1,30,'2020-07-08',2);
insert into Orders_2 values(4,2,10,'2020-06-15',2);
insert into Orders_2 values(5,2,40,'2020-07-01',10);
insert into Orders_2 values(6,3,20,'2020-06-24',2);
insert into Orders_2 values(7,3,30,'2020-06-25',2);
insert into Orders_2 values(9,3,30,'2020-05-08',3);

select o.customer_id, c.name
from Customers_2 c, Product_2 p, Orders_2 o
where c.customer_id = o.customer_id and p.product_id = o.product_id
group by o.customer_id, c.name
having ( 
	sum(case when o.order_date LIKE '2020-06%' then o.quality*p.price else 0 end)
	and
	sum(case when o.order_date LIKE '2020-07%' then o.quality*p.price else 0 end)
)
