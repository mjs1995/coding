select s.buyer_id
from Sales_4 as s
left join Product_5 as p on s.product_id = p.product_id
where p.product_name = 'S8' and s.buyer_id not in (select s.buyer_id
												   from Sales_4 s left join product_5 on s.product_id = p.product_id
												   where p.product_name = 'iPhone')
