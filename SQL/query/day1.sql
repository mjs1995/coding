CREATE TABLE member3(
ID  VARCHAR(30) NOT NULL,
gen bigint(30),
birth bigint(60) NOT NULL,
PRIMARY KEY(ID)
);


insert into member3 values ('MEM000001', 20, 1987);
insert into member3 values	('MEM000002', 20, 1988);
insert into member3 values	('MEM000003', 20, 1989);
insert into member3 values	('MEM000004', 20, 1990);
insert into member3 values	('MEM000005', 20, 1991);
insert into member3 values	('MEM000006', 10, 1992);
insert into member3 values	('MEM000007', 10, 1993);
insert into member3 values	('MEM000008', 10, 1994);
insert into member3 values	('MEM000009', 10, 1995);
insert into member3 values	('MEM000010', 10, 1996);
insert into member3 values	('MEM000011', NULL, 1997);
insert into member3 values	('MEM000012', NULL, 1998);

#--q1
select *
from member3

#--q2
with mbr as (
select mbr_base.ID as ID
, case when mbr_base.gen = '10' then '남'
	   when mbr_base.gen = '20' then '여'
       else '정보없음' end as gen #--as mbr_base.gen_sct_cd 성별
, case when year(current_date) - cast(mbr_base.birth as int) + 1 between 10 and 19 then '10대'
	   when year(current_date) - cast(mbr_base.birth as int) + 1 between 20 and 29 then '20대'
       when year(current_date) - cast(mbr_base.birth as int) + 1 between 20 and 29 then '30대'
       when year(current_date) - cast(mbr_base.birth as int) + 1 >= 40 then '40대이상'
       else '정보없음' end as age #-- 나이
from member3 as mbr_base
)
select ID as '회원'
	, gen as '성별'
	, age as '나이별'
from mbr;


# --q3
with mbr as (
select mbr_base.ID as ID
, case when mbr_base.gen = '10' then '남'
	   when mbr_base.gen = '20' then '여'
       else '정보없음' end as gen #--as mbr_base.gen_sct_cd 성별
, case when year(current_date) - cast(mbr_base.birth as int) + 1 between 10 and 19 then '10대'
	   when year(current_date) - cast(mbr_base.birth as int) + 1 between 20 and 29 then '20대'
       when year(current_date) - cast(mbr_base.birth as int) + 1 between 20 and 29 then '30대'
       when year(current_date) - cast(mbr_base.birth as int) + 1 >= 40 then '40대이상'
       else '정보없음' end as age #-- 나이
from member3 as mbr_base
) select mbr.gen as 성별
, count(mbr.ID) as 회원수
from mbr
group by mbr.gen ;
