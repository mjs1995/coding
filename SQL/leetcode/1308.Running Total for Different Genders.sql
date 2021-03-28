select t1.gender, t1.day, sum(t2.score_points) as total
from Scores as t1 inner join Scores as t2
on t1.gender = t2.gender
and t1.day>=t2.day
group by t1.gender, t1.day
