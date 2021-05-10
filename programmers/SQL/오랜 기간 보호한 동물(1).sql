select a.NAME, a.DATETIME
from ANIMAL_INS as a
left join ANIMAL_OUTS as b on a.ANIMAL_ID = b.ANIMAL_ID
where b.ANIMAL_ID is null 
order by DATETIME limit 3
