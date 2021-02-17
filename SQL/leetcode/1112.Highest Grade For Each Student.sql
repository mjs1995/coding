 create table Enrollments (
  	 student_id int,
	 course_id int,
	 grade int 
 );
 
 insert into Enrollments values(2,2,95);
 insert into Enrollments values(2,3,95);
 insert into Enrollments values(1,1,90);
 insert into Enrollments values(1,2,99);
 insert into Enrollments values(3,1,80);
 insert into Enrollments values(3,2,75);
 insert into Enrollments values(3,3,82);
 
select student_id, min(course_id), grade
from Enrollments
where (student_id, grade ) in
	(select student_id, max(grade)
	from Enrollments
	group by student_id)
group by student_id
order by student_id asc
