use day_39_widow_functions;
show tables;


select * from employees;

explain select * from employees where salary > 70000;


-- Single column index creation syntax | create index index_name on table_name(column_to_be_indexed)
create index idx_salary on employees(salary);


-- SQL to show all the indexes
show indexes from employees;

-- Compare query performance or cost of the queries
explain analyze select * from employees where salary > 70000;

-- Composite index creation
create index idx_dpt_salary on employees (department, salary);

-- Syntax to drop the index
drop index idx_salary on employees;


-- -> Index range scan on employees using idx_salary over (80000.00 < salary), 
-- with index condition: (employees.salary > 80000.00)  (cost=2.06 rows=4)
-- (actual time=0.0311..0.0449 rows=4 loops=1)









-- Index -> It is a special data structure that alllws the database to find rows much faster without scanning the entire table.







