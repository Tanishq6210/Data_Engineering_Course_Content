data = [
    (101, "Rahul", "Delhi", 5000),
    (102, "Priya", "Mumbai", 7000),
    (103, "Amit", "Bangalore", 3000),
    (104, "Neha", "Pune", 9000)
]

columns = ["customer_id", "name", "city", "balance"]

df = spark.createDataFrame(data, columns)

df.write.format("delta").mode("overwrite").save(
    "/output/customers_delta"
)

from delta.tables import DeltaTable

delta_table = DeltaTable.forPath(spark, "/output/customers_delta")

delta_table.update(
    condition = "customer_id = 102",
    set = {
        "balance" : "8500"
    }
)

delta_table.toDF().show()

delta_table.delete(condition = "customer_id = 104")
delta_table.toDF().show()

target = DeltaTable.forPath(spark, "/output/customers_delta")

source = [
    (102, "Priya", "Mumbai", 9500),
    (103, "Amit", "Hyderabad", 3000),
    (105, "Karan", "Delhi", 6000)
]

columns = ["customer_id", "name", "city", "balance"]

source_df = spark.createDataFrame(source, columns)
source_df.show()

# Merge -> It is a delta operation that allowws you to speify different actions based on matching conditions

# Upsert : A business / data operation pattern
target.alias("target").merge(
    source_df.alias("source"),
    "target.customer_id = source.customer_id"
).whenMatchedUpdate(
    set = {
        "name": "source.name",
        "city": "source.city",
        "balance": "source.balance"
    }
).whenNotMatchedInsert(
    values = {
        "customer_id" : "source.customer_id",
        "name": "source.name",
        "city": "source.city",
        "balance": "source.balance"
    }
).execute()



# .whenMatchedDelete(
#     condition = "source.status = 'DELETED'"
# )