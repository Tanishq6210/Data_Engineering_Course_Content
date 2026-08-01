select * from bank_balance;

-- LAG
select day_no, balance, lag(balance, 2, 0) over (order by day_no) as yesterday_balance from bank_balance;

-- LEAD
select day_no, balance, lead(balance, 1, 0) over (order by day_no) as yesterday_balance from bank_balance;

-- First_VALUE : It returns the first value inside the window
select * from sales;

select *, first_value(sales) over (order by sale_date) as first_value_numeric from sales;

-- Last value
select *, last_value(sales) over (order by sale_date rows between unbounded preceding and unbounded following) as last_value_numeric from sales;

-- Running Totals
select *, sum(revenue) over(order by sale_date) from sales;

-- Moving averages

select * from monthly_sales;

select month_name, sales, avg(sales) over( order by month_no rows between 2 preceding and current row) as moving_average_last_3_values from monthly_sales;



