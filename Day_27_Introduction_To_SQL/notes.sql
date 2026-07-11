-- Introduction to SQL Queries & Query Structure 
-- SELECT Statement                              
-- Column Aliasing (AS) & DISTINCT               
-- WHERE Clause (Comparison + Logical Operators) 
-- ORDER BY                                      
-- LIMIT                                         

-- Creating a table

-- describe employees;

-- Create database
-- create database data_engineering_course;

-- Use database
-- use data_engineering_course;

create table employees (
	emp_id int,
	emp_name varchar(20),
	emp_dept varchar(30),
	emp_salary int,
	emp_city varchar(30),
	emp_joining_date date
);

describe employees;

-- Inserting records in the table
insert into employees values 
(101, 'Manav', 'IT', 90000, 'Delhi', '2022-01-15'),
(102, 'Vibhore', 'IT', 10000, 'Delhi', '2022-01-15'),
(103, 'Manendar', 'Cyber', 50000, 'Delhi', '2022-01-15'),
(104, 'Aditi', 'HR', 100000, 'Delhi', '2022-01-15');

insert into employees values 
(105, 'Manav Gupta', 'IT', 1000000, 'Delhi', '2022-01-15');


-- SELECT statement
-- select column_name from table_name;
select * from employees;

-- column Aliasing (AS) : Alias changes only display
select emp_id as "Employee ID", emp_joining_date as "Joining Date" from employees;

-- Distinct keyword : Removed duplicate values
select distinct emp_dept from employees;

-- WHERE clause
select * from employees where emp_id != 102;
select emp_id, emp_name, emp_salary as "Salary" from employees 
where emp_salary >= 60000;

-- Comparison operators -> 
--  = , > , < , >= , <=, != or <>


-- Logical Operators 
-- AND, OR, NOT
select emp_id, emp_name from employees
where emp_dept = 'HR'
and emp_salary >= 120000;

select emp_id, emp_name from employees
where not emp_dept = 'HR' and emp_salary >= 60000;

-- Order By
select * from employees order by emp_salary desc;

-- LIMIT
select * from employees limit 2;