create table my_numbers (
	num int
);

insert into my_numbers values(8);
insert into my_numbers values(8);
insert into my_numbers values(3);
insert into my_numbers values(3);
insert into my_numbers values(1);
insert into my_numbers values(4);
insert into my_numbers values(5);
insert into my_numbers values(6);

select Max(num) num
from (SELECT num 
	FROM my_numbers 
	GROUP BY num 
	HAVING COUNT(*) = 1) as a;
