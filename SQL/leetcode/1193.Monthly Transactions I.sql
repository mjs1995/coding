create table Transactions(
 id             int     ,
 country        varchar ,
 state          varchar,
 amount         int     ,
 trans_date     date    
);

insert into Transactions values(121,'US','approved',1000,'2018-12-18');
insert into Transactions values(122,'US','declined',2000,'2018-12-19');
insert into Transactions values(123,'US','approved',2000,'2019-01-01');
insert into Transactions values(124,'DE','approved',2000,'2019-01-07');

select date_format(trans_date, '%Y-%m') as month, country,
	   count(id) as trans_count
	   sum(case when state='approved' then 1 else 0) as approved_count,
	   sum(amount) as trans_total_amount,
	   sum(case when state='approved' then amount else 0) as approved_total_amount
from Transactions
group by month,country
