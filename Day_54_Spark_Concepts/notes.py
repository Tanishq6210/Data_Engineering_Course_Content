import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable


from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = (
    SparkSession.builder
    .appName("Spark Concepts")
    .master("local[*]")
    .getOrCreate()
)

# spark.read
# spark.createDataFrame
# spark.read.csv
# spark.write

# rdd = spark.sparkContext.parallelize([
#     (101, "Tanishq", 24),
#     (102, "Rahul", 25),
#     (103, "Alice", 34)
# ])

# df = spark.createDataFrame(rdd, ["employee_id", "name", "age"])

# rdd.filter(lambda x: x[2] > 20)

# df.filter(df.age > 20)
# df1 = df.select("employee_id", "age")

# print(df1.show())
# print(rdd.collect())


# data = [
#     (101, "Tanishq", 24),
#     (102, "Rahul", 25),
#     (103, "Alice", 34)
# ]

# columns = ["id", "name", "age"]

# df = spark.createDataFrame(data, columns)

# df.show()

# df.printSchema()

# df = spark.read.option("header", True).option("inferSchema", True).csv("input/customers.csv")
# Explicit schema
schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("salary", DoubleType(), True),
    StructField("is_active", BooleanType(), True),
])

df = spark.read.option("header", True).schema(schema).csv("input/customers.csv")
df.explain()

# df = spark.read.schema(schema).json("input/customers.json")
# df.write.format("csv").save("output.csv")

# df.filter(df.age > 20) # "20" > 20

df.printSchema()

# Spark Datatypes:
# StringType() -> "Alice"
#IntegerType() -> 25
#DoubleType() -> 30.4
# DateType() -> "2024-01-03"
#TimestampType() -> "2024-01-03 12:30:45"
#BooleanType() -> True / False

# Parquet -> Columnar storage format