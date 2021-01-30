create table ActorDirector(
	actor_id    int,
	director_id int,
	timestamp   int
);

insert into ActorDirector values(1,1,0);
insert into ActorDirector values(1,1,1);
insert into ActorDirector values(1,1,2);
insert into ActorDirector values(1,2,3);
insert into ActorDirector values(1,2,4);
insert into ActorDirector values(2,1,5);
insert into ActorDirector values(2,1,6);

select actor_id, director_id
from ActorDirector
group by actor_id, director_id
having count(1) >= 3
