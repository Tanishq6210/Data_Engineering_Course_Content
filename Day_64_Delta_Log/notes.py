# Google Collab Code

# 1. Install required libraries
# !pip install -q pyspark==3.5.3 delta-spark==3.2.0

from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

builder = (
    SparkSession.builder
    .appName("Class12_Delta_Lake")
    .config(
        "spark.sql.extensions",
        "io.delta.sql.DeltaSparkSessionExtension"
    )
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog"
    )
)

spark = configure_spark_with_delta_pip(builder).getOrCreate()

data = [
    (1, "Rahul", "Delhi", 5000),
    (2, "Priya", "Mumbai", 7000),
    (3, "Aman", "Bangalore", 6000)
]

columns = ["customer_id", "name", "city", "amount"]

df = spark.createDataFrame(data, columns)
df.show()

df.write.mode("overwrite").parquet("/output/customers_parquet")

df.write.format("delta").mode("overwrite").save("/output/customers_delta")

delta_df = spark.read.format("delta").load("/output/customers_delta")
delta_df.show()

delta_df = spark.read.format("delta").load("/output/customers_delta")
delta_df.show()

from delta.tables import DeltaTable

delta_table = DeltaTable.forPath(spark, "/output/customers_delta")
delta_table.update(
    condition = "customer_id = 1",
    set = {"amount" : "5500"}
)

delta_table.toDF().show()

delta_df = spark.read.format("delta").load("/output/customers_delta")
delta_df.show()