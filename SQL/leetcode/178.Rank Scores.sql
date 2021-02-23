create table Scores(
	id int,
	score float
);

insert into Scores values(1, 3.50);
insert into Scores values(2, 3.60);
insert into Scores values(3, 4.00);
insert into Scores values(4, 3.85);
insert into Scores values(5, 4.00);
insert into Scores values(6, 3.65);

Select DISTINCT(Score)
from Scores
order by Score desc

select Score, (select Count(Distinct Score) from Scores where Score >= s.Score) as Rank
From Scores s
order by Score Desc;
