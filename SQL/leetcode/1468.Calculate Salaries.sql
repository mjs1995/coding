select s.company_id, s.employee_id, s.employee_name,
	round(case when salary_max < 1000 then s.salary
		 	   when salary_max >= 1000 and salary_max <= 10000 then s.salary * 0.76
		       else s.salary * 0.51 end, 0) as salary
from Salaries inner join (
	select company_id, max(salary) as salary_max
	from Salaries
	group by company_id) as t)
on s.company_id = t.company_id
