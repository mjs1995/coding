-- 627. Swap Salary
update Salary
set sex = case
    when sex = 'f' then 'm'
    ELSE 'f'
    END;
    
-- 196. Delete Duplicate Emails
DELETE FROM Person
where id NOT IN (
select sub.min_id
from (
select email, MIN(id) as min_id
from Person
group by email
) sub 
);

delete p1
from Person p1
  inner join Person p2 on p1.Email = p2.Email
where p1.Id > p2.Id;
