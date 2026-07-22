select * from Customers;
select * from Orders;


select * from Orders inner join Customers on Customers.customerId = Orders.customerId;

-- Give me all the customers and their order information if exists
select * from Customers right join Orders on Customers.customerId = Orders.customerId;
select * from Orders left join Customers on Customers.customerId = Orders.customerId;

insert into Orders values (1007, null, null, null, null);

select * from Customers full outer join Orders on Customers.customerId = Orders.orderId;

select c.customerName, o.orderId from Customers c left join Orders o on c.customerId = o.customerId
union
select c.customerName, o.orderId from Customers c right join Orders o on c.customerId = o.customerId;

select * from customers left join orders on customers.customerId = orders.customerId;

-- how to get customers who have placed on order -> inner join
-- how to get all the customer irrespective of their order status -> left join
-- how to get all the customer who have not placed an order -> left join + null check on the right table's foreign key


select c.customerName, o.orderId from customers c left join orders o on c.customerId = o.customerId where o.orderId is null;

-- Difference in on clause and where clause
-- SQL -> 
-- FROM -> JOIN -> ON -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT


select * from customers c left join orders o on c.customerId = o.customerId;
select * from customers c left join orders o on c.customerId = o.customerId and o.amount > 5000; 

select * from customers c left join orders o on c.customerId = o.customerId where o.amount > 500;