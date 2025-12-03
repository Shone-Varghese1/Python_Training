select first_name,last_name,city
from students;

select * from students
where city="Alappuzha";

select * from students order by age desc;

-- update and delete

update students
set city="Chennai"
where student_id=1;

update students 
set age =24
where email ="hari@example.com";

delete from students where student_id=3;

delete from students where city="banglore";

drop table students;
drop database college_db




