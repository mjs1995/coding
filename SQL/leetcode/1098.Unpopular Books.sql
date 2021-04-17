select book_id, name
from Books
where book_id not in (
	select book_id
	from Orders
	where dispatch_date >= '2018-06-23' and dispatch_date <= '2019-06-22'
	group by book_id
	having sum(quantity) >= 10)
) and available_from < '2019-05-23'
