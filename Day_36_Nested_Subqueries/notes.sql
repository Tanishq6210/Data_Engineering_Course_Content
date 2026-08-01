-- Subquery - It is a SQL query written inside another SQL query
-- 
-- It is also known as
-- Nested Query
-- Inner Query
-- Inner select

-- Syntax of a subquery
select col1, col2, col3 from table_name where column_name operator (
	select -------
);

-- Step 1 - Find the average salary of the class (Scalar subquery)
select avg(salary) from employees;

-- Step 2 - find employees where salary is above 69300
select * from employees where salary > 69300;

-- Subquery
-- Find the employees where salary is greater than average salary of the employees
select * from employees where salary > (select avg(salary) from employees);

-- Find the employee whose salary is maximum salary
select * from employees order by salary desc limit 1;

-- Find the employee whose salary is maximum salary using subquery
-- Step 1: 
select max(salary) from employees;

-- Step 2: Find the employee whose salary is 95k
select * from employees where salary = 95000;

select * from employees where salary = (select max(salary) from employees);


select * from employees;

select * from departments;

-- Find all the employees who are living in Delhi
select e.* from employees e join departments d on e.department_id = d.department_id where d.city = 'Delhi';


-- Step 1: Find out the department_ids which are in city Delhi
select department_id from departments where city = 'Delhi';

-- Step 2: Find all the employees who are working in either department (101, 104)
select * from employees where department_id in (101, 104);

select * from employees where department_id in (select department_id from departments where city = 'Delhi');


-- Subquery in select
-- Give me the employee names, salary, avg_salary

-- Step 1: Find avg salary
select avg(salary) from employees; 


-- STep 2: Fetch the relevant rows
select employee_name, salary, 69300 as company_average from employees;


select employee_name, salary, (select max(salary) from employees) as max_salary from employees;


-- Group the employees by department_id and find average salary for each department
select department_id, avg(salary) as avg_salary from employees group by department_id;

select dept_avg.department_id  from (
	select department_id, avg(salary) as avg_salary from employees group by department_id
) as dept_avg;


-- SHow only departments whose average salary exceeds 80000
select * from (
	select department_id, avg(salary) as avg_salary from employees group by department_id
) as dept_avg where avg_salary > 69300;

select department_id, avg(salary) as avg_salary from employees group by department_id having avg(salary) > 69300;


-- ANY keyword usecase -> compare against any one value
1001 < any (1000, 2000, 3000)

-- ALL keyword -> condition must satisfy every value
1001 > all (1000, 2000, 3000);

-- IN keyword
1001 in (1001, 1002, 1003)

-- 50k, 61k
select * from employees  where salary > any (1000, 2000);



select * from employees;