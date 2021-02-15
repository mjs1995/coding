CREATE TABLE Project (
  project_id INT,
  employee_id  INT
);

CREATE TABLE Employee (
	employee_id       INT,
	name varchar,
	experience_years int
);

INSERT INTO Project VALUES (1,1);
INSERT INTO Project VALUES (1,2);
INSERT INTO Project VALUES (1,3);
INSERT INTO Project VALUES (2,1);
INSERT INTO Project VALUES (2,4);

INSERT INTO Employee  VALUES ( 1, 'Khaled',3);
INSERT INTO Employee  VALUES ( 2, 'Ali',2);
INSERT INTO Employee  VALUES ( 3, 'John',1);
INSERT INTO Employee  VALUES ( 4, 'Doe',2);


select project_id, employee_id
from Project
join Employee
using (employee_id)
where (project_id, experience_years) in (
    select project_id, max(experience_years)
    from Project
    join Employee
    using (employee_id)
    group by project_id)
