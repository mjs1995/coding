create table Users (
	user_id int,
	named varchar
);

insert into Users values(1,'aLice');
insert into Users values(2, 'boB');

select user_id, concat(Upper(substring(named,1,1)),Lower(substring(named,2,length(named)))) as name
from Users
order by user_id
