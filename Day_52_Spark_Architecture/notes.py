import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import spark_partition_id

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

spark = (
    SparkSession.builder.appName("Spark Architecture")
         .master("local[*]")
         .getOrCreate()
)


print("Spark session started!")


data = [
    ("Delhi", 1000),
    ("Delhi", 1500),
    ("Mumbai", 2000),
    ("Mumbai", 3000),
    ("Bangalore", 2500),
    ("Delhi", 1200),
]

df = spark.createDataFrame(data, ["city", "amount"])

df.show()

print(f'Number of partitions: {df.rdd.getNumPartitions()}')

df2 = df.repartition(4)
print(f"Number of partitions after repartitioning: {df2.rdd.getNumPartitions()}")

df2.withColumn(
    "partition_id",
    spark_partition_id()
).show()

df.count()