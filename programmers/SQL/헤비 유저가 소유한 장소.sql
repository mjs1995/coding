SELECT A.ID,A.NAME,	A.HOST_ID
from PLACES as A
RIGHT JOIN (
    select * FROM PLACES
    group by HOST_ID
    having count(HOST_ID) >= 2
) as b
on a.HOST_ID = B.HOST_ID
order by a.ID
