create table Products (
	product_id int,
	new_price int,
	change_date date
);

insert into Products values(1, 20,'2019-08-14');
insert into Products values(2, 50,'2019-08-14');
insert into Products values(1, 30,'2019-08-15');
insert into Products values(1, 35,'2019-08-16');
insert into Products values(2, 65,'2019-08-17');
insert into Products values(3, 20,'2019-08-18');

SELECT A.product_id, 
CASE WHEN M.new_price IS NULL THEN 10 ELSE M.new_price END AS price
FROM
(SELECT DISTINCT product_id FROM Products) A
LEFT JOIN
(SELECT product_id, new_price, 
ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rnk
FROM Products
WHERE change_date <= '2019-08-16') M
ON A.product_id = M.product_id
WHERE rnk = 1 OR rnk IS NULL
ORDER BY price DESC
