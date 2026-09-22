import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    explode,
    posexplode,
    array_contains,
    size,
    element_at,
    to_date,
    to_timestamp,
    year,
    month,
    dayofmonth,
    datediff,
    upper,
    udf,
    sum as spark_sum,
    count,
    when,
)
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    LongType,
    ArrayType,
    MapType,
    DoubleType,
)


spark = SparkSession.builder.appName("Class_9_ComplexJson").getOrCreate()

events_path = "data/events.json"

df = (
    spark.read
    .option("multiLine", True)
    .json(events_path)
)

df.printSchema()
df.show(truncate = False)

# Flattening -> If I have a struct, I can simply extract it's individual fields

flat_df = df.select(
    "event_id",
    "user_id",
    col("user.name").alias("user_name"),
    col("user.city").alias("user_city"),
    col("device.type").alias("device_type"),
    col("device.os").alias("device_os")
).show(truncate = False)

# Arrays
functions_arrays = """
array_contains(), size(), element_at()
"""

# array_contains()
df.filter(array_contains("tags", "mobile"))
# size()

df.select(
    "event_id",
    size("tags").alias("number_of_tags")
)
# element_at
df.select(
    "event_id",
    element_at("tags", 1).alias("first_tag") #1 - based indexing
)


# Explode
exploded_df = df.select(
    "event_id",
    "user_id",
    explode("events").alias("event")
)

exploded_df.show(truncate = False)

exploded_flattened_df = exploded_df.select(
    "event_id",
    "user_id",
    col("event.event_type").alias("event_type"),
    col("event.product_id").alias("product_id"),
    col("event.price").alias("price")
).show(truncate = False)

# Posexplode()

df.select(
    "event_id",
    posexplode("tags").alias("position", "tag")
).show()

# Date & Timestamp Handling
df = df.withColumn("event_timestamp", to_timestamp("event_timestamp"))

# to_date
df.withColumn("event_timestamp", to_date("event_timestamp"))

df.select(year("event_timestamp").alias("year"))
df.select(month("event_timestamp").alias("month"))
df.select(dayofmonth("event_timestamp").alias("day_of_month"))

df.withColumn(
    "days_since_signup",
    datediff("purchase_date", "signupdate") # Difference in days
)

# UDF -> User Defined Functions
upper("user_name")

decryptPAN("pan_values")

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def make_upper(name):
    return name.upper()

upper_udf = udf(make_upper, StringType())

df.withColumn(
    "upper_name",
    upper_udf("user_name")
).show()