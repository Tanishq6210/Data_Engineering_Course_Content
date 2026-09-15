import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum


spark = SparkSession.builder \
    .appName("Class7A_Join_Practical") \
    .getOrCreate()


# ============================================================
# 1. CUSTOMERS
# ============================================================

customers_data = [
    (1, "Rahul", "Bangalore"),
    (2, "Priya", "Mumbai"),
    (3, "Amit", "Delhi"),
    (4, "Neha", "Hyderabad"),
    (5, "Arjun", "Pune"),
    (6, "Sneha", "Chennai")
]

customers = spark.createDataFrame(
    customers_data,
    ["customer_id", "customer_name", "city"]
)

c = customers.alias("c")

# ============================================================
# 2. ORDERS
# ============================================================

orders_data = [
    (101, 1, 1001, 2500),
    (102, 2, 1002, 1800),
    (103, 1, 1003, 3200),
    (104, 3, 1004, 1500),
    (105, 4, 1005, 4500),
    (106, 7, 1006, 2200),
    (101, 1, 1001, 4000)
]

orders = spark.createDataFrame(
    orders_data,
    ["order_id", "customer_id", "product_id", "amount"]
)

o = orders.alias("o")

# ============================================================
# 3. PRODUCTS
# ============================================================

products_data = [
    (1001, "Laptop"),
    (1002, "Wireless Mouse"),
    (1003, "Keyboard"),
    (1004, "Monitor"),
    (1005, "Headphones"),
    (1007, "Smartphone")
]

products = spark.createDataFrame(
    products_data,
    ["product_id", "product_name"]
)

p = products.alias("p")
# ============================================================
# DISPLAY DATA
# ============================================================

# print("CUSTOMERS")
# customers.show()

# print("ORDERS")
# orders.show()

# print("PRODUCTS")
# products.show()

# Join Syntax -> df1.join(df2, condition, how)
# customer_order_inner_join_result = customers.join(orders, 
#                                                   (customers.customer_id == orders.customer_id) & (orders.amount >= 2000), 
#                                                   "inner"
#                                                   )


# customer_order_inner_join_result.show()

# customer_order_left_join_result = customers.join(orders, (customers.customer_id == orders.customer_id) & (orders.order_id.isNull()),  "left")

# customer_order_left_join_result.show()


# customer_order_right_join_result = customers.join(orders, customers.customer_id == orders.customer_id, "right")
# customer_order_right_join_result.show()

# order_customer_left_join_result = orders.join(customers, customers.customer_id == orders.customer_id, "left")
# order_customer_left_join_result.show()

customer_order_full_outer_join = customers.join(orders, customers.customer_id == orders.customer_id, "full")

customer_order_full_outer_join.show()

# Join using alias
c_o_full_outer_join = c.join(
    o,
    c.customer_id == o.customer_id,
    "inner"
)
co = c_o_full_outer_join.alias("co")
# c_o_full_outer_join.show()


# Duplicate columns

c_o_full_outer_join = c.join(
    o,
    c.customer_id == o.customer_id,
    "inner"
).drop(c.customer_id)

# c_o_full_outer_join.show()



# Multiple Joins

# c_o_p_inner_join = co.join(p, co.product_id == p.product_id, "inner")
# c_o_p_inner_join.show()

c_o_p_inner_join_single_statement = (
    c.join(o, c.customer_id == o.customer_id, "inner")
    .join(p, o.product_id == p.product_id, "inner")
    .select(
        c.customer_id,
        c.customer_name,
        o.order_id,
        p.product_name
    )
)


# Usecase 1 -> The business wants to know how much money each customer has spent | gb - c_id and sum_total
# Usecase 2 -> The company wants to identify customers who places orders frequently | gb - c_id and count
# Usecase 3 -> The company wans to know how much revenue each product generated | join -> product, order , gb -> product_id , agg -> amount

# Hint: Use aggregation and grouping and joins
# orders.groupBy("customer_id").agg(sum(orders.amount).alias("total_spent")).show()

# Usecase 1
# customer_spending = c.join(
#     o,
#     c.customer_id == o.customer_id,
#     "inner"
# ).groupBy(
#     c.customer_id,
#     c.customer_name
# ).agg(
#     sum(o.amount).alias("total_spent")
# ).show()

# Usecase 2
order_count = c.join(
    o,
    c.customer_id == o.customer_id,
    "inner"
).groupBy(
    c.customer_id,
    c.customer_name
).count()


# Usecase 3 answer
product_sales = o.join(
    p,
    o.product_id == p.product_id,
    "inner"
).groupBy(
    p.product_id,
    p.product_name
).agg(
    sum(o.amount).alias("total_sales")
).orderBy("total_sales", ascending = False).show()

# Syntax
# Join -> Grouping -> Aggregation -> OrderBy 