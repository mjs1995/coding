create table Friendship (
 user1_id       int     ,
 user2_id       int     
);

create table Likes (
 user_id      int     ,
 page_id      int     
);

insert into Friendship values(1,2);
insert into Friendship values(1,3);
insert into Friendship values(1,4);
insert into Friendship values(2,3);
insert into Friendship values(2,4);
insert into Friendship values(2,5);
insert into Friendship values(6,1);

insert into Likes values(1,88);
insert into Likes values(2,23);
insert into Likes values(3,24);
insert into Likes values(4,56);
insert into Likes values(5,11);
insert into Likes values(6,33);
insert into Likes values(2,77);
insert into Likes values(3,77);
insert into Likes values(6,88);

select distinct page_id as recommended_page
from Likes
where user_id in (select user2_id
				  from Friendship
				  where user1_id = 1
				  union
				  select user1_id
				  from Friendship
				  where user2_id = 1)
	and page_id not in (select page_id
					    from Likes
					    where user_id = 1)
