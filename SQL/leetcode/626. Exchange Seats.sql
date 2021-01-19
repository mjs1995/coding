# https://leetcode.com/problems/exchange-seats/
select (case when mod(id,2) = 1 and id != (select count(*) from seat) then id+1
        when mod(id,2) = 0 then id-1
        else id end) id, student
from seat
order by id asc;
