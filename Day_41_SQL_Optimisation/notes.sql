show tables;

select * from employees;

explain select * from employees where salary > 70000;

explain analyze select * from employees where salary = 80000;

-- Index syntax
create index idx_salary on employees(salary);

-- -> Index range scan on employees using idx_salary over (80000.00 < salary), 
-- with index condition: (employees.salary > 80000.00)  (cost=2.06 rows=4)
-- (actual time=0.0311..0.0449 rows=4 loops=1)


