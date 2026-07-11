-- Table Creation and Constraints
use data_engineering_course;

-- Table : It is a collection of related information stored in rows and columns
show tables;
select * from employees;

-- Flipkart
-- Orders -> order_id (int), order_name(varchar), order_price(Float / Decimal), customer_id(INT), order_address(TEXT), order_time(TIMESTAMP), order_date (Date), Comments

-- SQL Data types
-- int, varchar -> String (maximum length), TEXT, Date (YYYY-MM-DD), Timestamp -> Date + Time, Boolean

-- 2025-07-15 14:30:45

-- create table table_name (column_name_1 datatype_1, column_name_2 datatype_2)

create table students (
	student_id int primary key,
	name varchar (100) not null,
	about text,
	date_of_birth date,
	created_at timestamp,
	is_active boolean,
	email varchar(100) unique,
	phone_number varchar(10) unique,
	age int check(age > 0)
)

drop table students;

describe students;


-- Constraints -> Rules to prevent invalid data
-- Primary -> NOT NULL, UNIQUE (Eg. StudentID, EmployeeID, AadharNumber, PassportNumber, RollNo)
-- NOT NULL
-- Unique
-- CHECK Constraint


-- Foreign Key : It refers to the primary key of another table
create table users(
	user_id int primary key,
	name varchar(100)
)

describe users;

create table orders(
	order_id int primary key,
	user_id int,
	foreign key(user_id) references users(user_id)
)

describe orders;

-- Data Manipulation -> insert, update, delete

-- Insertion : insert into table_name values ();
insert into users values (1, 'Tanishq');
insert into users values (2, 'Saurabh');
insert into users values (3, NULL);
insert into orders values(101, 1);
insert into orders values(102, 1);
insert into orders values(103, 2);

select * from users;
select * from orders;

-- Updation: update table_name set column_name=new_value where user_id = value
update users set user_id = 3 where name = 'Tanishq';


-- Deletion: delete from table_name where column_name_pk = value
delete from users where user_id = 2;
delete from orders where user_id = 2;



Introduction to Tables & Data 
SQL Data Types
Creating Tables & Constraints
Foreign Key Introduction
INSERT, UPDATE, DELETE
Constraint Violation Exercises
