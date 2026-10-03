# 1 - Configuration
dbutils.widgets.text(
    "input_path",
    "",
    "Input Path"
)

input_path = dbutils.widgets.get("input_path")


dbutils.widgets.text(
    "output_path",
    "",
    "Output Path"
)

output_path = dbutils.widgets.get("output_path")

# Section 2 - Ingestion

df_raw = spark.read.csv(
    input_path,
    header=True,
    inferSchema=True
)

display(df_raw)

# Section 3 - Data Quality
from pyspark.sql.functions import col

df_clean = df_raw.filter(
    (col("quantity") > 0) & (col("price") > 0)
)

print(df_clean.count())

# Section 4 - Transformation
df_transformed = df_clean.withColumn("total_amount", col("quantity") * col("price"))

display(df_transformed)

# Section 5 - SQL Analysis
# select product, sum(total_amount) as revenue from orders group by product order by revenue desc;


# Section 6 - Output
df_transformed.write.format("delta").mode("overwrite").save(output_path)


# Section 7 - Validation
df_output = spark.read.format("delta").load(output_path)

display(df_output)