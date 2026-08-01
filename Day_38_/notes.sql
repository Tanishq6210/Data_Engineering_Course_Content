-- CTE syntax

-- with cte_name as (
-- 	query
-- )
-- main_query

-- Important points
-- A cte
-- 1. has a name
-- 2. It contains a select query
-- 3. It behaves like a temporary table


select * from customers;
select * from orders;
-- Calculate total purchase for every customer - Without CTE
select customer_id, sum(amount) from orders group by customer_id;

-- With CTE

with total_sales as (
	select customer_id, sum(amount) from orders group by customer_id
) 

select * from total_sales;

-- Execution order -> WITH -> CTE Creation -> Main select -> Result -> CTE deletion

select * from orders where amount > 5000;

with high_orders as (
	select * from orders o where amount > 5000
)

select * from high_orders;

-- Nested subquery
select * from (
	select customer_id, sum(amount) total_sales from orders group by customer_id
) x where total_sales > 10000;



with sales as (
	select customer_id, sum(amount) total_sales from orders group by customer_id
)

select * from sales where total_sales > 10000;

-- Cleaner, Readable and Reusable

-- Employee -> salary -> department -> Bonus -> Tax -> Experience -> final
-- 
-- EmployeeSalary -> BonusCalculation -> TaxCalculation -> Final


-- Multiple CTEs

-- with
-- 
-- A as (.....),
-- B as (.....),
-- C as (.....)
-- 
-- select ...

-- Step 1: Calculate sales
with sales as (
	select customer_id, sum(amount) total_sales from orders group by customer_id
)

-- Step 2 -> Find Premium Customers
with Premium as (
	select * from sales where total_sales > 10000
)


-- Step 3: Main query
select c.customer_name, p.total_sales from Premium p join customers c on p.customer_id = c.customer_id;




with sales as (
	select customer_id, sum(amount) total_sales from orders group by customer_id
),
Premium as (
	select * from sales where total_sales > 10000
)

select c.customer_name premium_customer_name, p.total_sales from Premium p join customers c on p.customer_id = c.customer_id;

-- Orders -> Sales -> Premium -> join customers -> Output


-- Recursive CTE
-- Syntax
with recursive cte_name as (
	base_query
	
	union all
	
	recursive query
)
select * fromm cte_name;

-- Example: Numbers 1 - 5
with recursive numbers as (
	select 1 as n
	
	union all
	
	select n + 1 from numbers where n < 5
)

select * from numbers;
