create table Prices (
	product_id int,
	start_date date,
	end_date date,
	price int
);

create table UnitsSold (
	product_id int,
	purchase_date date,
	units int
);

insert into Prices values(1,'2019-02-17','2019-02-28',5);
insert into Prices values(1,'2019-03-01','2019-03-22',20);
insert into Prices values(2,'2019-02-01','2019-02-20',15);
insert into Prices values(2,'2019-02-21','2019-03-31',30);

insert into UnitsSold values(1,'2019-02-25',100);
insert into UnitsSold values(1,'2019-03-01',15);
insert into UnitsSold values(2,'2019-02-10',200);
insert into UnitsSold values(2,'2019-03-22',30);

select a.product_id, round(sum(units * price) / sum(units), 2) as average_price
from UnitsSold a inner join Prices b on a.product_id = b.product_id
and a.purchase_date between b.start_date and b.end_date
group by a.product_id
