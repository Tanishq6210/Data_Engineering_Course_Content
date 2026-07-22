-- select columns 
-- from table_1 
-- join table_2 on condition_1
-- join table_3 on condition_2
-- join table_4 on condition_4;

select * from customers;
select * from orders;
select * from products;
select * from orderdetails;

select c.customer_name, o.order_id, p.product_name, od.quantity
from customers c
join orders o on c.customer_id = o.customer_id
join orderdetails od on o.order_id = od.order_id
join products p on od.product_id = p.product_id;


select * from orders o join orderdetails od on o.order_id = od.order_id;

-- Multiple joins -> Aggregation -> To represent multiple rows as a single row
select o.order_id, sum(quantity) from orders o join orderdetails od on o.order_id = od.order_id group by o.order_id;


-- Self Join
select * from employees;
select e.employee_name as Employee, m.employee_name as Manager from employees e left join employees m on e.manager_id = m.employee_id;

-- Non Equi Joins
describe salarygrade;
select * from salarygrade;
select * from employees;
select * from products;
select * form orderdetails;
select * from orderdetails od join products p on od.product_id = p.product_id;

select e.employee_name, e.salary, g.grade from employees e join salarygrade g on e.salary between g.min_salary and g.max_salary;


-- Business requirement -> customer name, total orders, total quantity, total amount

select c.customer_id, count(distinct o.order_id) as total_orders, 
sum(od.quantity) as total_items, sum(od.quantity * p.price) as total_amount
from customers c
join orders o on c.customer_id = o.customer_id
join orderdetails od on o.order_id = od.order_id
join products p on od.product_id = p.product_id
group by c.customer_id;
