-- inner join
SELECT e.emp_id,e.emp_name,d.dept_name,d.location
from employees e
inner join departments d
on e.dept_id=d.dept_id;


-- left join
select e.emp_id,e.emp_name,d.dept_name
from employees e
left join departments d
on e.dept_id=d.dept_id;

-- right join
select e.emp_id,e.emp_name,d.dept_name
from employees e
right join departments d
on e.dept_id=d.dept_id;
-- full join
select e.emp_id,e.emp_name,d.dept_name
from employees e
left join departments d
on e.dept_id=d.dept_id
union
select e.emp_id,e.emp_name,d.dept_name
from employees e
right join departments d
on e.dept_id=d.dept_id;
-- cross join gives every mapping possible

select e.emp_name,d.dept_name
from employees e
cross join departments d;



