-- Syntax of group by

-- select aggregate_function(column_name) from table_name group by grouping_column_name;

select * from employees;

-- I need to get the average salary of each department
select department, avg(salary) from employees where city = 'Bangalore' group by department;
select department, sum(salary) from employees where city = 'Bangalore' group by department;
select department, min(salary) from employees where city = 'Bangalore' group by department;
select department, max(salary) from employees where city = 'Bangalore' group by department;

-- Rules of Group by
-- Rule 1 - every selected column must either 
-- 1. be grouped
-- 2. be aggregated
-- Note: Every non aggregated column must appear inside the group by clause

select department, avg(salary) from employees group by department;

-- Rule 2: Aggregate functions don't need group by (Entire table becomes 1 group)
select avg(salary) from employees;

-- Rule 3: Group by clause return one row per group

-- Get count of the employees on the bases of department and city
select city, department, count(*) from employees group by city, department;



-- Where -> It filters rows
-- Having -> It filters groups

-- Execution order
-- Table -> where -> remaining rows -> group by -> groups -> having -> remaining groups
-- Find employees earning above 50000
select * from employees where salary > 50000;

-- Find departments whose average salary is above 50000
select department from employees group by department having avg(salary) > 50000;


-- Execution order
-- from -> where -> group by -> avg -> having -> select -> order by -> limit


-- Common mistakes (ye apko nhi karna hai)
-- 1. selecting a column that is neither grouped nor aggregated
-- 2. using where with an aggregated function
-- 3. forgetting group by

select * from employees;
select department, sum(salary) from employees;

select department , avg(salary) from employees group by department having department = 'IT';

