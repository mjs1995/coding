create table NPV (
	id           int,     
	year         int,    
	npv          int   
);

create table Queries(
	id int,
	year int
);

insert into NPV values(1,2018,100);
insert into NPV values(7,2020,30);
insert into NPV values(13,2019,40);
insert into NPV values(1,2019,113);
insert into NPV values(2,2008,121);
insert into NPV values(3,2009,12);
insert into NPV values(11,2020,99);
insert into NPV values(7,2019,0);

insert into Queries values(1,2019);
insert into Queries values(2,2008);
insert into Queries values(3,2009);
insert into Queries values(7,2018);
insert into Queries values(7,2019);
insert into Queries values(7,2020);
insert into Queries values(13,2019);

select Queries.id, Queries.year, ifnull(npv, 0) as npv
    from Queries left join NPV
    on Queries.id = NPV.id and Queries.year = NPV.year
    order by Queries.id;
