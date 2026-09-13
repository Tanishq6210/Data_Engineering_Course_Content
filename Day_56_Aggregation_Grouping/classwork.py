# ============================================================
# CLASS 6 - PYSPARK PRACTICAL DATASET
# E-COMMERCE DATA
# ============================================================

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

print("ORDERS")
orders_df.show()


# ============================================================
# 5. BASIC DATAFRAME INFORMATION
# ============================================================

print("CUSTOMERS SCHEMA")
customers_df.printSchema()

print("PRODUCTS SCHEMA")
products_df.printSchema()

print("ORDERS SCHEMA")
orders_df.printSchema()


# ============================================================
# 6. COUNT - TOTAL NUMBER OF ORDERS
# ============================================================

total_orders = orders_df.count()

print("Total Orders:", total_orders)


# ============================================================
# 7. SUM - TOTAL QUANTITY SOLD
# ============================================================

orders_df.select(
    sum("quantity").alias("total_quantity_sold")
).show()


# ============================================================
# 8. JOIN ORDERS WITH PRODUCTS
# ============================================================

order_details = orders_df.join(
    products_df,
    on="product_id",
    how="inner"
)

print("ORDERS + PRODUCTS")
order_details.show()


# ============================================================
# 9. CALCULATE REVENUE
# ============================================================

order_details = order_details.withColumn(
    "revenue",
    col("quantity") * col("price")
)

print("ORDER DETAILS WITH REVENUE")
order_details.show()


# ============================================================
# 10. TOTAL REVENUE
# ============================================================

order_details.select(
    sum("revenue").alias("total_revenue")
).show()


# ============================================================
# 11. AVERAGE REVENUE
# ============================================================

order_details.select(
    avg("revenue").alias("average_revenue")
).show()


# ============================================================
# 12. MINIMUM REVENUE
# ============================================================

order_details.select(
    min("revenue").alias("minimum_revenue")
).show()


# ============================================================
# 13. MAXIMUM REVENUE
# ============================================================

order_details.select(
    max("revenue").alias("maximum_revenue")
).show()


# ============================================================
# 14. MULTIPLE AGGREGATIONS
# ============================================================

order_details.select(
    count("order_id").alias("total_orders"),
    sum("revenue").alias("total_revenue"),
    avg("revenue").alias("average_revenue"),
    min("revenue").alias("minimum_revenue"),
    max("revenue").alias("maximum_revenue")
).show()


# ============================================================
# 15. GROUP BY REGION
# ============================================================

order_customer = orders_df.join(
    customers_df,
    on="customer_id",
    how="inner"
)

print("ORDERS + CUSTOMERS")

order_customer.show()


# ============================================================
# 16. NUMBER OF ORDERS BY REGION
# ============================================================

order_customer.groupBy(
    "region"
).count().show()


# ============================================================
# 17. REVENUE BY CATEGORY
# ============================================================

order_details.groupBy(
    "category"
).agg(
    sum("revenue").alias("total_revenue")
).show()


# ============================================================
# 18. AVERAGE REVENUE BY CATEGORY
# ============================================================

order_details.groupBy(
    "category"
).agg(
    avg("revenue").alias("average_revenue")
).show()


# ============================================================
# 19. MULTIPLE AGGREGATIONS BY CATEGORY
# ============================================================

order_details.groupBy(
    "category"
).agg(
    count("order_id").alias("total_orders"),
    sum("revenue").alias("total_revenue"),
    avg("revenue").alias("average_revenue"),
    min("revenue").alias("minimum_revenue"),
    max("revenue").alias("maximum_revenue")
).show()


# ============================================================
# 20. REVENUE BY PRODUCT
# ============================================================

order_details.groupBy(
    "product_id",
    "product_name"
).agg(
    sum("revenue").alias("total_revenue")
).show()


# ============================================================
# 21. TOP PRODUCTS BY REVENUE
# ============================================================

order_details.groupBy(
    "product_id",
    "product_name"
).agg(
    sum("revenue").alias("total_revenue")
).orderBy(
    "total_revenue",
    ascending=False
).show()


# ============================================================
# 22. REVENUE BY REGION
# ============================================================

order_region = order_details.join(
    customers_df,
    on="customer_id",
    how="inner"
)

order_region.groupBy(
    "region"
).agg(
    sum("revenue").alias("total_revenue")
).show()


# ============================================================
# 23. TOP REGIONS BY REVENUE
# ============================================================

order_region.groupBy(
    "region"
).agg(
    sum("revenue").alias("total_revenue")
).orderBy(
    "total_revenue",
    ascending=False
).show()


# ============================================================
# 24. GROUP BY MULTIPLE COLUMNS
# REGION + CATEGORY
# ============================================================

order_region.groupBy(
    "region",
    "category"
).agg(
    sum("revenue").alias("total_revenue")
).orderBy(
    "total_revenue",
    ascending=False
).show()


# ============================================================
# 25. AVERAGE ORDER VALUE
# ============================================================

order_value = order_details.groupBy(
    "order_id"
).agg(
    sum("revenue").alias("order_value")
)

order_value.select(
    avg("order_value").alias("average_order_value")
).show()


# ============================================================
# 26. TOP 5 ORDERS BY VALUE
# ============================================================

order_value.orderBy(
    "order_value",
    ascending=False
).show(5)


# ============================================================
# 27. CREATE TEMPORARY VIEWS FOR SPARK SQL
# ============================================================

orders_df.createOrReplaceTempView("orders")

products_df.createOrReplaceTempView("products")

customers_df.createOrReplaceTempView("customers")

order_details.createOrReplaceTempView("order_details")


# ============================================================
# 28. SPARK SQL - DISPLAY ORDERS
# ============================================================

spark.sql("""
    SELECT *
    FROM orders
""").show()


# ============================================================
# 29. SPARK SQL - TOTAL NUMBER OF ORDERS
# ============================================================

spark.sql("""
    SELECT COUNT(*) AS total_orders
    FROM orders
""").show()


# ============================================================
# 30. SPARK SQL - TOTAL QUANTITY SOLD
# ============================================================

spark.sql("""
    SELECT SUM(quantity) AS total_quantity_sold
    FROM orders
""").show()


# ============================================================
# 31. SPARK SQL - TOTAL REVENUE
# ============================================================

spark.sql("""
    SELECT SUM(revenue) AS total_revenue
    FROM order_details
""").show()


# ============================================================
# 32. SPARK SQL - AVERAGE REVENUE
# ============================================================

spark.sql("""
    SELECT AVG(revenue) AS average_revenue
    FROM order_details
""").show()


# ============================================================
# 33. SPARK SQL - REVENUE BY CATEGORY
# ============================================================

spark.sql("""
    SELECT
        category,
        SUM(revenue) AS total_revenue
    FROM order_details
    GROUP BY category
""").show()


# ============================================================
# 34. SPARK SQL - REVENUE BY CATEGORY
# SORTED DESCENDING
# ============================================================

spark.sql("""
    SELECT
        category,
        SUM(revenue) AS total_revenue
    FROM order_details
    GROUP BY category
    ORDER BY total_revenue DESC
""").show()


# ============================================================
# 35. SPARK SQL - ORDERS BY REGION
# ============================================================

spark.sql("""
    SELECT
        c.region,
        COUNT(*) AS total_orders
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    GROUP BY c.region
""").show()


# ============================================================
# 36. SPARK SQL - REVENUE BY REGION
# ============================================================

spark.sql("""
    SELECT
        c.region,
        SUM(o.quantity * p.price) AS total_revenue
    FROM orders o
    JOIN products p
        ON o.product_id = p.product_id
    JOIN customers c
        ON o.customer_id = c.customer_id
    GROUP BY c.region
    ORDER BY total_revenue DESC
""").show()


# ============================================================
# 37. SPARK SQL - REVENUE BY REGION + CATEGORY
# ============================================================

spark.sql("""
    SELECT
        c.region,
        p.category,
        SUM(o.quantity * p.price) AS total_revenue
    FROM orders o
    JOIN products p
        ON o.product_id = p.product_id
    JOIN customers c
        ON o.customer_id = c.customer_id
    GROUP BY
        c.region,
        p.category
    ORDER BY total_revenue DESC
""").show()


# ============================================================
# 38. SPARK SQL - TOP 5 PRODUCTS
# ============================================================

spark.sql("""
    SELECT
        p.product_name,
        SUM(o.quantity * p.price) AS total_revenue
    FROM orders o
    JOIN products p
        ON o.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_revenue DESC
    LIMIT 5
""").show()


# ============================================================
# 39. SPARK SQL - MULTIPLE AGGREGATIONS
# ============================================================

spark.sql("""
    SELECT
        COUNT(*) AS total_orders,
        SUM(revenue) AS total_revenue,
        AVG(revenue) AS average_revenue,
        MIN(revenue) AS minimum_revenue,
        MAX(revenue) AS maximum_revenue
    FROM order_details
""").show()


# ============================================================
# 40. STOP SPARK SESSION
# ============================================================

# spark.stop()