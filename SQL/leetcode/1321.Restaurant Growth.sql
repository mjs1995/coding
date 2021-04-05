create table Customer_1(
 customer_id    int     ,
 name           varchar ,
 visited_on     date    ,
 amount         int     
);

insert into Customer_1 values(1,'Jhon','2019-01-01',100);
insert into Customer_1 values(2,'Daniel','2019-01-02',110);
insert into Customer_1 values(3,'Jade','2019-01-03',120);
insert into Customer_1 values(4,'Khaled','2019-01-04',130);
insert into Customer_1 values(5,'Winston','2019-01-05',110);
insert into Customer_1 values(6,'Elvis','2019-01-06',140);
insert into Customer_1 values(7,'Anna','2019-01-07',150);
insert into Customer_1 values(8,'Maria','2019-01-08',80);
insert into Customer_1 values(9,'Jaze','2019-01-09',110);
insert into Customer_1 values(1,'Jhon','2019-01-10',130);
insert into Customer_1 values(3,'Jade','2019-01-10',150);

select a.visited_on , sum(b.amount) as amount, round(avg(b.amount),2) as average_amount   
from (select visited_on, sum(amount) as amount 
	  from Customer_1 group by visited_on) a
join (select visited_on, sum(amount) as amount
	  from Customer_1 group by visited_on) b on datediff(a.visited_on, b.visited_on) between 0 and 6 
group by a.visited_on
having count(b.amount) = 7
