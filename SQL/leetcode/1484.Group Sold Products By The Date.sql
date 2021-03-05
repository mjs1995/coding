create table Activities (
	sell_date date,
	product varchar
);

insert into Activities values('2020-05-30', 'Headphone');
insert into Activities values('2020-06-01', 'Pencil');
insert into Activities values('2020-06-02', 'Mask');
insert into Activities values('2020-05-30', 'Basketball');
insert into Activities values('2020-06-01', 'Bible');
insert into Activities values('2020-06-02', 'Mask');
insert into Activities values('2020-05-30', 'T-Shirt');

SELECT sell_date, COUNT(DISTINCT product) AS num_sold, 
GROUP_CONCAT(DISTINCT product ORDER BY product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
