CREATE TABLE Employee1 (
  employee_id INT,
  team_id     INT
);

insert into Employee1 values(1,8);
INSERT INTO Employee1 (employee_id, team_id) VALUES(2,8);
INSERT INTO Employee1 (employee_id, team_id) VALUES(3,8);
INSERT INTO Employee1 (employee_id, team_id) VALUES(4,7);
INSERT INTO Employee1 (employee_id, team_id) VALUES(5,9);
INSERT INTO Employee1 (employee_id, team_id) VALUES(6,9);

select *
from Employee1

#해당 종목 그룹 카운트를 각 라인에 맞춰서 보여줌
select employee_id,
	count(*) over (partition by team_id) as team_size
from Employee1
order by employee_id;
