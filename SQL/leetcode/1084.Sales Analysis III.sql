create table Sales_4 (
 seller_id    int,     
 product_id   int,    
 buyer_id     int,     
 sale_date    date,    
 quantity    int,     
 price        int     
);

create table Product_5(
 product_id    int,     
 product_name  varchar, 
 unit_price    int     
);


insert into Sales_4 values(1,1,1,'2019-01-21',2,2000);
insert into Sales_4 values(1,2,2,'2019-02-17',1,800);
insert into Sales_4 values(2,2,3,'2019-06-02',1,800);
insert into Sales_4 values(3,3,4,'2019-05-13',2,2800);

insert into Product_5 values(1,'S8',1000);
insert into Product_5 values(2,'G4',800);
insert into Product_5 values(3,'iPhone',1400);

select s.product_id, p.product_name
from Sales_4 as s
join Product_5 as p on s.product_id = p.product_id
group by s.product_id, p.product_name
having min(s.sale_date) >= '2019-01-01' and
	   max(s.sale_date) <= '2019-03-31'
