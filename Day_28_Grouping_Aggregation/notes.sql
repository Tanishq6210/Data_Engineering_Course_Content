-- Aggregations & Grouping

use data_engineering_course;
describe employees;

select * from employees;

-- Aggregate functions (Summary functions)-> These function take multiple rows as input and return a single summarized value.
-- 1. Count -> It counts the number of rows
select count(*) as Total_Employees from employees;

-- 2. SUM -> It adds all the numeric values
select sum(salary) as Total_Salary from employees;

-- 3. Average  -> AVG (It gives the average value)
select avg(salary) as Average_Salary from employees;

-- 4. Minimum -> 
select min(salary) as Minimum_Salary from employees;

-- 5. Maximum -> 
select max(salary) as Maximum_Salary from employees;

-- Group By
select * from employees;
-- Question : What is the average salary of each department

select avg(salary) as Average_Salary from employees;

select department, avg(salary) as "Average Salary"
from employees
group by department ;

-- To get the sum of the salaries of each department
select department, sum(salary) as "Total Salary"
from employees
group by department ;


-- HAVING Clause -> Filtering the groups
-- WHERE clause -> Filtering of rows
select * from employees;
-- Find the departments where the number of employees are more than or equal to 3
select department, count(*) as total_employees from employees
group by department having count(*) >= 3;

select department, avg(salary) from employees 
where salary >= 40000
group by department 
having avg(salary) >= 60000;

-- WHERE -> Should a row participate
-- HAVING -> Should this group appear in the final result