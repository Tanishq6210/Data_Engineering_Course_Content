show tables;

select * from employees;

-- Normal aggregate function problem
select *, avg(salary) as avg_salary from employees;

-- Window function -> Over()
select *, avg(salary) over() as avg_salary from employees;

-- Count the number of employees in each department 
select *, avg(salary) over() as total_dept_sal from employees group by department;

-- Topic 2 -> Partition By (Create groups but keeps the rows intact)
-- Syntax:
-- select ....., aggr(column_name) over(partition by column_Name) from table_name

select * from employees;
show tables;

select *, avg(salary) over(partition by department) avg_dept_sal from employees;

select employee_id, salary, sum(salary) over(partition by department) avg_dept_sal from employees;




-- Maximum marks for each department and the employee_name
select employee_name, department, max(salary) over(partition by department) max_dept_salary from employees;

-- Topic 3 - order by inside window
select employee_name, department, salary, 
row_number() over(partition by department order by salary desc) as salary_order 
from employees;


-- row_number -> rank()

select employee_name, department, salary, 
rank() over(partition by department order by salary desc) as salary_order 
from employees;


-- rank() -> dense_rank()
select employee_name, department, salary, 
dense_rank() over(partition by department order by salary desc) as salary_order 
from employees order by salary_order;


-- Topic 4 - ntile [Quartiles - 1]
-- ntile(4)
-- Quartile 1 -> top 25%
-- Quartile 2 -> next 25%
-- Quartile 3 -> next 25%
-- Quartile 4 -> bottom 25%

select * from customers c ;

select customer_name, total_purchase, ntile(4) over(order by total_purchase desc) from customers;
