create table Products2 (
	product_id int,
	low_fats char,
	recyclable char
);

insert into Products2 values(0,'Y','N');
insert into Products2 values(1,'Y','Y');
insert into Products2 values(2,'N','Y');
insert into Products2 values(3,'Y','Y');
insert into Products2 values(4,'N','N');

select product_id
from Products2
where low_fats = 'Y' and recyclable = 'Y'; 
