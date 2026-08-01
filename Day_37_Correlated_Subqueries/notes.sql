-- Find employees earning above their department average

show tables;

select * from employees e ;
select e1.EmployeeName, e1.DepartmentId, e1.Salary from employees e1
where salary > (
	select avg(salary) from employees e2 where e2.DepartmentID = e1.DepartmentID
);

select avg(salary) from employees where DepartmentID = 3;

-- Understanding exists
-- Check if a customer has placed any order

select * from customers;
select * from orders;


-- Correlated Subquery
select * from customers c
where exists (
	select customerName from orders o
	where o.CustomerID = c.CustomerID 
)

-- Normal subquery using IN
select * from customers c
where customerId IN (
	select customerId from orders
);


-- NOT Exists -> It return rows where subquery returns nothing

-- Find customers who have not placed an order
-- 1. Anti-join
select * from customers c
where not exists (
	select * from orders o where o.CustomerID = c.CustomerID 
)

-- Anti Join Logic
select * from customers c left join orders o on c.CustomerID  = o.CustomerID where o.CustomerID is null;

