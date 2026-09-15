import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast


spark = SparkSession.builder \
    .appName("Class7B_Shuffle_Broadcast") \
    .getOrCreate()

spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.autoBroadcastJoinThreshold", 50)

orders_data = [
    (101, "C1", 500),
    (102, "C2", 800),
    (103, "C1", 300),
    (104, "C3", 700),
    (105, "C2", 900),
    (106, "C4", 400),
    (107, "C1", 600),
    (108, "C3", 350),
    (109, "C5", 1200),
    (110, "C2", 450)
]

customers_data = [
    ("C1", "Rahul", "Bangalore"),
    ("C2", "Priya", "Delhi"),
    ("C3", "Amit", "Mumbai"),
    ("C4", "Sneha", "Pune"),
    ("C5", "Arjun", "Chennai")
]

orders = spark.createDataFrame(
    orders_data,
    ["order_id", "customer_id", "amount"]
)

customers = spark.createDataFrame(
    customers_data,
    ["customer_id", "name", "city"]
)

o = orders.alias("o")
c = customers.alias("o")

o.join(c, o.customer_id == c.customer_id, "inner").explain("formatted")

print("------------------------------------")

o.join(broadcast(c), o.customer_id == c.customer_id, "inner").explain("formatted")