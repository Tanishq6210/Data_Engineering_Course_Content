# ============================================================
# CLASS 13B — DELTA INCREMENTAL PIPELINE & TIME TRAVEL
# Complete PySpark Practical — Google Colab
# ============================================================


# IMPORTANT:
# After this cell finishes:
# Runtime → Restart session
#
# Then run this cell again from the beginning.
# ============================================================


# ============================================================
# 2. START SPARK WITH DELTA LAKE
# ============================================================

from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
from delta.tables import DeltaTable

builder = (
    SparkSession.builder
    .appName("Class13B")
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

print("Spark Version:", spark.version)
print("Delta Lake configured successfully!")


# ============================================================
# 3. CREATE INITIAL CUSTOMER DATA
# ============================================================

path = "/content/customer_delta"

columns = [
    "customer_id",
    "name",
    "city",
    "phone"
]

initial_data = [
    (101, "Tanishq", "Bangalore", "9999999999"),
    (102, "Rahul", "Delhi", "8888888888"),
    (103, "Ankit", "Mumbai", "7777777777")
]

initial_df = spark.createDataFrame(
    initial_data,
    columns
)

print("\nInitial Customer Data:")
initial_df.show()


# ============================================================
# 4. CREATE INITIAL DELTA TABLE
# ============================================================

initial_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save(path)

customer_delta = DeltaTable.forPath(
    spark,
    path
)

print("Initial Delta Table:")
customer_delta.toDF().show()


# ============================================================
# 5. CREATE INCREMENTAL DATA
#
# 101 → Existing customer → UPDATE
# 104 → New customer      → INSERT
# ============================================================

incremental_data = [
    (101, "Tanishq", "Hyderabad", "9999999999"),
    (104, "Priya", "Chennai", "6666666666")
]

incremental_df = spark.createDataFrame(
    incremental_data,
    columns
)

print("\nIncremental Data:")
incremental_df.show()


# ============================================================
# 6. MERGE — INCREMENTAL LOAD / UPSERT
# ============================================================

(
    customer_delta.alias("target")
    .merge(
        incremental_df.alias("source"),
        "target.customer_id = source.customer_id"
    )
    .whenMatchedUpdate(
        set={
            "name": "source.name",
            "city": "source.city",
            "phone": "source.phone"
        }
    )
    .whenNotMatchedInsert(
        values={
            "customer_id": "source.customer_id",
            "name": "source.name",
            "city": "source.city",
            "phone": "source.phone"
        }
    )
    .execute()
)

print("\nAfter Incremental MERGE:")
customer_delta.toDF().show()


# ============================================================
# 7. VIEW DELTA TABLE HISTORY
# ============================================================

print("\nDelta Table History:")

history = customer_delta.history()

history.select(
    "version",
    "timestamp",
    "operation"
).show(truncate=False)


# ============================================================
# 8. TIME TRAVEL
#    READ TABLE BEFORE THE MERGE
# ============================================================

current_version = (
    history
    .select("version")
    .orderBy("version", ascending=False)
    .first()["version"]
)

previous_version = current_version - 1

print("Current Version:", current_version)
print("Reading Previous Version:", previous_version)

old_df = (
    spark.read
    .format("delta")
    .option("versionAsOf", previous_version)
    .load(path)
)

print("\nData Before MERGE:")
old_df.show()


# ============================================================
# 9. SIMULATE ACCIDENTAL DELETE
# ============================================================

customer_delta.delete(
    "customer_id = 103"
)

print("\nAfter Accidental DELETE:")
customer_delta.toDF().show()


# ============================================================
# 10. TIME TRAVEL — VIEW DATA BEFORE DELETE
# ============================================================

history = customer_delta.history()

delete_version = (
    history
    .select("version")
    .orderBy("version", ascending=False)
    .first()["version"]
)

version_before_delete = delete_version - 1

print("Delete Version:", delete_version)
print("Version Before Delete:", version_before_delete)

before_delete_df = (
    spark.read
    .format("delta")
    .option("versionAsOf", version_before_delete)
    .load(path)
)

print("\nData Before DELETE:")
before_delete_df.show()


# ============================================================
# 11. RESTORE PREVIOUS VERSION
# ============================================================

customer_delta.restoreToVersion(
    version_before_delete
)

print("\nAfter RESTORE:")
customer_delta.toDF().show()


# ============================================================
# 12. CHECK FINAL HISTORY
# ============================================================

print("\nFinal Delta Table History:")

customer_delta.history() \
    .select(
        "version",
        "timestamp",
        "operation"
    ) \
    .show(truncate=False)


# ============================================================
# 13. OPTIMIZATION / COMPACTION
# ============================================================

print("\nAttempting OPTIMIZE / COMPACTION...")

try:

    result = customer_delta.optimize().executeCompaction()

    print("Optimization / Compaction completed:")
    result.show(truncate=False)

except Exception as e:

    print("OPTIMIZE API is not available in this environment.")
    print("Concept:")
    print("OPTIMIZE compacts many small files into fewer larger files.")


# ============================================================
# 14. FINAL DELTA TABLE
# ============================================================

print("\nFinal Customer Table:")
customer_delta.toDF().show()


# ============================================================
# 15. FINAL SUMMARY
# ============================================================

print("""
============================================================
CLASS 13B PRACTICAL COMPLETE
============================================================

What we demonstrated:

1. Created an initial Delta table
2. Created incremental source data
3. Used MERGE for UPDATE + INSERT
4. Viewed Delta table history
5. Used Time Travel
6. Simulated an accidental DELETE
7. Viewed data from a previous version
8. Restored a previous version
9. Viewed the new transaction history
10. Demonstrated OPTIMIZE / Compaction

Key Concept:

Delta Lake
    |
    +-- Parquet data files
    |
    +-- _delta_log
            |
            +-- Version 0
            +-- Version 1
            +-- Version 2
            +-- ...

Every transaction creates a new table version.
Time Travel allows us to read an earlier version.
RESTORE creates a new transaction that brings the table
back to the state of an earlier version.
============================================================
""")