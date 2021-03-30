select a.player_id, a.event_date , sum(a.games_played) as games_played_so_far
from Activity a inner join Activity b on a.player_id = b.player_id
where a.event_date >= b.event_date
group by a.player_id,a.event_date 
order by a.player_id,a.event_date
