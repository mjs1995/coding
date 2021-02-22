create table Candidate (
	id int,
	Name varchar
);

create table Vote (
	id int,
	CandidateId int
);

insert into Candidate values(1,'A');
insert into Candidate values(2,'B');
insert into Candidate values(3,'C');
insert into Candidate values(4,'D');
insert into Candidate values(5,'E');

insert into Vote values(1,2);
insert into Vote values(2,4);
insert into Vote values(3,3);
insert into Vote values(4,2);
insert into Vote values(5,5);

select Name
from Candidate
where id = (select CandidateId
		   from Vote
		   group by CandidateId
		   order by count(1) desc
		   limit 1)
