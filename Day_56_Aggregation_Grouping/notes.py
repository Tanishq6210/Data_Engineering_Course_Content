import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    sum,
    avg,
    min,
    max,
    count
)

# ============================================================
# 1. CREATE SPARK SESSION
# ============================================================

spark = SparkSession.builder \
    .appName("Class6_Aggregation_Practical") \
    .getOrCreate()


# ============================================================
# 2. CUSTOMERS DATA
# ============================================================

customers_data = [
    (101, "Aarav", "North"),
    (102, "Diya", "South"),
    (103, "Kabir", "East"),
    (104, "Anaya", "West"),
    (105, "Rohan", "North"),
    (106, "Ishita", "South"),
    (107, "Arjun", "East"),
    (108, "Meera", "West"),
    (109, "Vivaan", "North"),
    (110, "Sara", "South"),
    (111, "Aditya", "East"),
    (112, "Kiara", "West")
]

customers_columns = [
    "customer_id",
    "customer_name",
    "region"
]

customers_df = spark.createDataFrame(
    customers_data,
    customers_columns
)

print("CUSTOMERS")
customers_df.show()


# ============================================================
# 3. PRODUCTS DATA
# ============================================================

products_data = [
    (201, "Laptop", "Electronics", 65000),
    (202, "Smartphone", "Electronics", 35000),
    (203, "Headphones", "Electronics", 2500),
    (204, "Keyboard", "Accessories", 1800),
    (205, "Mouse", "Accessories", 900),
    (206, "Backpack", "Lifestyle", 2200),
    (207, "Running Shoes", "Fashion", 4500),
    (208, "T-Shirt", "Fashion", 1200),
    (209, "Smart Watch", "Electronics", 8000),
    (210, "Water Bottle", "Lifestyle", 700)
]

products_columns = [
    "product_id",
    "product_name",
    "category",
    "price"
]

products_df = spark.createDataFrame(
    products_data,
    products_columns
)

print("PRODUCTS")
products_df.show()


# ============================================================
# 4. ORDERS DATA
# ============================================================

orders_data = [
    (1001, 101, 201, 1, "2026-08-01"),
    (1002, 102, 202, 2, "2026-08-01"),
    (1003, 103, 203, 3, "2026-08-02"),
    (1004, 104, 204, 2, "2026-08-02"),
    (1005, 105, 205, 4, "2026-08-03"),
    (1006, 106, 206, 2, "2026-08-03"),
    (1007, 107, 207, 1, "2026-08-04"),
    (1008, 108, 208, 3, "2026-08-04"),
    (1009, 109, 209, 1, "2026-08-05"),
    (1010, 110, 210, 5, "2026-08-05"),
    (1011, 101, 202, 1, "2026-08-06"),
    (1012, 102, 201, 1, "2026-08-06"),
    (1013, 103, 205, 2, "2026-08-07"),
    (1014, 104, 207, 2, "2026-08-07"),
    (1015, 105, 203, 4, "2026-08-08"),
    (1016, 106, 209, 1, "2026-08-08"),
    (1017, 107, 206, 3, "2026-08-09"),
    (1018, 108, 210, 4, "2026-08-09"),
    (1019, 109, 204, 2, "2026-08-10"),
    (1020, 110, 208, 2, "2026-08-10"),
    (1021, 111, 201, 1, "2026-08-11"),
    (1022, 112, 202, 2, "2026-08-11"),
    (1023, 101, 209, 1, "2026-08-12"),
    (1024, 102, 203, 5, "2026-08-12"),
    (1025, 103, 207, 1, "2026-08-13"),
    (1026, 104, 206, 2, "2026-08-13"),
    (1027, 105, 210, 6, "2026-08-14"),
    (1028, 106, 205, 3, "2026-08-14"),
    (1029, 107, 208, 4, "2026-08-15"),
    (1030, 108, 204, 3, "2026-08-15")
]

orders_columns = [
    "order_id",
    "customer_id",
    "product_id",
    "quantity",
    "order_date"
]

orders_df = spark.createDataFrame(
    orders_data,
    orders_columns
)

# Dataframe API's

# Aggregation
# 1. count() -> To get the total count or total no. of rows
# print(f"Total orders: {orders_df.count()}")
# orders_df.count()

# 2. sum() - To get the total sum
# orders_df.select(sum("quantity").alias("total_quantity")).show()

# 3. avg() - To get the average value of the column
# orders_df.select(avg("quantity").alias("avg_quantity")).show()

# 4. min() - To get the minimum value
# orders_df.select(min("quantity").alias("min_quantity")).show()

# 4. max() - To get the maximum value
# orders_df.select(max("quantity").alias("max_quantity")).show()

# Multiple aggregation functions
# orders_df.select(
#     sum("quantity").alias("total_quantity"),
#     avg("quantity").alias("avg_quantity"),
#     min("quantity").alias("min_quantity"),
#     max("quantity").alias("max_quantity")
# ).show()


# Grouping
# 1. groupBy() - It is used to group the data base on one or more columns

# products_df.groupBy("category").max("price").alias("max_price").show()
# products_df.groupBy("category").min("price").alias("min_price").show()
# products_df.groupBy("category").avg("price").alias("average_price").show()
# products_df.groupBy("category").sum("price").alias("total_price").show()


# Multiple aggregation with groupBy()

# products_df.groupBy("category").agg(
#     count("product_id").alias("total_products"),
#     min("price").alias("min_price"),
#     max("price").alias("max_price"),
#     avg("price").alias("average_price"),
#     sum("price").alias("total_price")
# ).show()

# Grouping by multiple columns
# products_df.groupBy("category", "product_name").max("price").alias("max_price").show()

# Ordering
# products_df.groupBy("category").max("price").alias("toal_price").orderBy("total_price", ascending = True).show()

# Spark SQL - Instead of learning an entirely new analytical language, Spark allows you to use SQL against ditributed datasets
# Temporary Views: Before writing SQL against a dataframe, we need to make it available to Spark SQL


# Spark SQL
orders_df.createOrReplaceTempView("orders")
products_df.createOrReplaceTempView("products")


spark.sql("""
    select * from orders
""").show()

spark.sql("""
    select sum(amount) as total_revenue from orders
""").show()

spark.sql("""
    select count(*) as total_orders from orders
""").show()

spark.sql("""
    select category, max(price) as max_price from products group by category order by max_price asc
""").show()