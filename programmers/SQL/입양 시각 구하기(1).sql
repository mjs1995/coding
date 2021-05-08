select hour(datetime) as HOUR, count(datetime) as COUNT
from ANIMAL_OUTS 
group by HOUR
having HOUR >= 9 and HOUR <= 19
order by HOUR
