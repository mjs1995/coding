create table Users_1 (
 user_id        int,     
 name           varchar, 
 mail           varchar 
);

insert into Users_1 values(1,'Winston','winston@leetcode.com');
insert into Users_1 values(2,'Jonathan','jonathanisgreat');
insert into Users_1 values(3,'Annabelle','bella-@leetcode.com');
insert into Users_1 values(4,'Sally','sally.come@leetcode.com');
insert into Users_1 values(5,'Marwan','quarz#2020@leetcode.com');
insert into Users_1 values(6,'David','david69@gmail.com');
insert into Users_1 values(7,'Shapiro','.shapo@leetcode.com');

select * from Users_1
where mail regexp  '^[a-zA-Z]+[a-zA-Z0-9_\\./\\-]{0,}@leetcode\\.com$' 
order by user_id
