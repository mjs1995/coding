(select name as results
from Movie_Ratinig natural join Users
group by Users.user_id
order by count(*) desc, name asc
limit 1)
union
(select Movies.title as results
from Movie_Rating natural join Movies
where month(created_at) = '2'
group by Movies.movie_id
order by avg(rating) desc, title asc
limit 1)
