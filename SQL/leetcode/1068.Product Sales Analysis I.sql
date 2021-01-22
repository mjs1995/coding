CREATE TABLE Sales (
  sale_id INT,
  product_id INT,
  years  INT,
  quantity INT,
  price INT
);

CREATE TABLE Product (
	product_id INT,
	product_name varchar
);

INSERT INTO Sales VALUES ( 1, 100, 2008, 10, 5000);
INSERT INTO Sales VALUES ( 2, 100, 2009, 12, 5000);
INSERT INTO Sales VALUES ( 7, 200, 2011, 15, 9000);

INSERT INTO Product VALUES ( 100, 'Nokia');
INSERT INTO Product VALUES ( 200, 'Apple');
INSERT INTO Product VALUES ( 300, 'Samsung');


select b.product_name, a.year, a.price 
from Sales as a
join Product as b on a.product_id = b.product_id;
