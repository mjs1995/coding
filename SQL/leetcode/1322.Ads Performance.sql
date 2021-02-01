create table Ads(
	ad_id          int,
	user_id        int,    
	action         varchar
);

insert into Ads values(1,1,'Clicked');
insert into Ads values(2,2,'Clicked');
insert into Ads values(3,3,'Viewed');
insert into Ads values(5,5,'Ignored');
insert into Ads values(1,7,'Ignored');
insert into Ads values(2,7,'Viewed');
insert into Ads values(3,5,'Clicked');
insert into Ads values(1,4,'Viewed');
insert into Ads values(2,11,'Viewed');
insert into Ads values(1,2,'Clicked');

select ad_id,ifnull(round(sum(action='Clicked')/ sum(action !='Ignored')*100,2),0) as ctr
from ads group by ad_id
order by ctr desc,ad_id

