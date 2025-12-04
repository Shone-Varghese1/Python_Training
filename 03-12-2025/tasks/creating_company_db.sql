create database company_db;
use company_db;


create table departments(
dept_id int primary key,
dept_name varchar(50),
location varchar(50)
);
create table employees(
emp_id int primary key,
emp_name varchar(50),
email varchar(50),
salary int,
dept_id int null
);

iNSERT INTO departments (dept_id, dept_name, location)
VALUES
(10, 'HR', 'Mumbai'),
(20, 'Finance', 'Delhi'),
(30, 'IT', 'Bangalore'),
(40, 'Marketing', 'Chennai'),
(50, 'Admin', 'Hyderabad');   -- no employees for dept 50
 
 
INSERT INTO employees (emp_id, emp_name, email, salary, dept_id)
VALUES
(101, 'Aisha Khan', 'aisha@company.com', 60000, 10),
(102, 'Rahul Sharma', 'rahul@company.com', 72000, 20),
(103, 'Meera Iyer', 'meera@company.com', 50000, 30),
(104, 'Imran Ali', 'imran@company.com', 65000, NULL),  -- no department
(105, 'Sanjay Patel', 'sanjay@company.com', 45000, NULL), -- no department
(106, 'David John', 'david@company.com', 90000, 40);




