select * from orders;
select * from archivedorders;

describe orders;
describe archivedorders;

-- Insertion
-- We will copy the data from 1 table to another
-- Syntax -> 
-- insert into destination_table select col1, col2, col3.... from source_table where condition;

insert into archivedorders select * from orders where orderDate < '2024-01-01';

-- Update
update products set price = price + 100 where product_id = 1;

select * from customers;
select * from orders;

select * from orders o join customers c on o.customerId = c.customerId ;
update orders o join customers c on o.customerId = c.customerId set o.discount = 20 where c.membership = 'Gold';

-- Deletion
-- I need to delete the invalid orders from the order table
select * from orders_nofk;
select * from customers;

-- delete from table_name where condition;

select * from orders_nofk o left join customers c on o.customerId = c.customerId;
delete o from orders_nofk o left join customers c on o.customerId = c.customerId where c.customerId is null;

-- Delete b/w Truncate
-- It can delete rows on the basis of a condition
delete from customers;

-- Entire table becomes empty (All the rows will be deleted) 
truncate table orders;

-- Drop : The existence of the table will be deleted
drop table orders;

-- Foreign key helps you achieving the referential integrity
select * from orders;



select * from customers;
select * from orders;

-- Insert Anomaly
insert into orders values (1008, 100, '2024-01-01', null , NULL);

-- Update Anomaly
update orders set customerId = 100 where orderId = 1001;

-- Delete Anomaly
delete from customers where customerId = 1;

-- Ways to  Avoid delete anomalies
-- 1. Restrict
create table orders_1 (
	orderId int primary key,
	customerId int,
	foreign key (customerId) references customers(customerId) on delete restrict
)

-- 2. Cascade
create table orders_2 (
	orderId int primary key,
	customerId int,
	foreign key (customerId) references customers(customerId) on delete cascade
) 

select * from orders;

delete from orders where customerId = 2;
delete from customers where customerId = 2;
select * from customers;

insert into orders_3 values (102, 2);

select * from orders_3;
-- 3. SET NULL
create table orders_3 (
	orderId int primary key,
	customerId int,
	foreign key (customerId) references customers(customerId) on delete set null
) 

delete from customers where customerId = 2;