create table TVProgram(
 program_date   date,    
 content_id     int,     
 channel        varchar 	
);

create table Content1(
 content_id        int, 
 title             varchar, 
 Kids_content      varchar,    
 content_type      varchar 
);

insert into TVProgram values('2020-06-10 08:00',1,'LC-Channel');
insert into TVProgram values('2020-05-11 12:00',2,'LC-Channel');
insert into TVProgram values('2020-05-12 12:00',3,'LC-Channel');
insert into TVProgram values('2020-05-13 14:00',4,'Disney Ch');
insert into TVProgram values('2020-06-18 14:00',4,'Disney Ch');
insert into TVProgram values('2020-07-15 16:00',5,'Disney Ch');

insert into Content1 values(1,'Leetcode Movie','N','Movies');
insert into Content1 values(2,'Alg. for Kids','Y','Series');
insert into Content1 values(3,'Database Sols','N','Series');
insert into Content1 values(4,'Aladdin','Y','Movies');
insert into Content1 values(5,'Cinderella','Y','Movies');

select distinct a.title 
from Content1 a 
join TVProgram b ON a.content_id = b.content_id
WHERE a.content_type = 'Movies' 
and a.Kids_content = 'Y'
and (b.program_date between '2020-06-01' and '2020-06-30');

