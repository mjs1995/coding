create table point (
	x int
);

insert into point values (-1);
insert into point values (0);
insert into point values (2);

SELECT MIN(p2.x - p1.x) AS shortest 
FROM point AS p1, 
	 point AS p2 
WHERE p1.x < p2.x;
