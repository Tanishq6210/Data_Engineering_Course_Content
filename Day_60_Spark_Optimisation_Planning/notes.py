import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark import StorageLevel

spark = SparkSession.builder \
    .appName("Class6_Aggregation_Practical") \
    .getOrCreate()


from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkOptimizationDemo") \
    .getOrCreate()

orders_data = [
    (101, 1, 5000,  "SUCCESS"),
    (102, 2, 15000, "SUCCESS"),
    (103, 3, 25000, "FAILED"),
    (104, 1, 12000, "SUCCESS"),
    (105, 4, 3000,  "SUCCESS"),
    (106, 5, 20000, "SUCCESS"),
    (107, 2, 8000,  "SUCCESS"),
    (108, 3, 18000, "SUCCESS"),
    (109, 6, 22000, "FAILED"),
    (110, 4, 11000, "SUCCESS")
]

orders_columns = [
    "order_id",
    "customer_id",
    "amount",
    "status"
]

orders = spark.createDataFrame(
    orders_data,
    orders_columns
)

orders.show()

customers_data = [
    (1, "Tanishq", "Bangalore"),
    (2, "Rahul",   "Delhi"),
    (3, "Priya",   "Mumbai"),
    (4, "Aman",    "Pune"),
    (5, "Neha",    "Hyderabad"),
    (6, "Rohan",   "Chennai")
]

customers_columns = [
    "customer_id",
    "customer_name",
    "city"
]

customers = spark.createDataFrame(
    customers_data,
    customers_columns
)

customers.show()

customers_needed_columns = customers.select("customer_id", "city") # Column pruning
orders_needed_columns = orders.filter(orders.amount > 1000).select("customer_id", "amount") #Column pruning & predicate pushdown

result = (
    orders
    # .filter(orders.amount > 10000) #Predicate pushdown
    .join(customers, "customer_id")
    # .select(
    #     "customer_id",
    #     "amount",
    #     "city"
    # )
)
print("--------------Extended--------------------")
result.explain(extended = True)
print("--------------Formatted---------------------------")
result.explain("formatted")
result.show()




# -----------------------------------
# Scenario 1 - Good candidate
# df = spark.read.parquet("sales/")

# filtered_df = df.filter(df.amount > 1000) #Will execution start at this point ?


# filtered_df.cache() 

# filtered_df.count() #Action 1 - Job 1

# filtered_df.groupBy("city").count() #Action 2 - Job 2

# filtered_df.groupBy("product").sum("amount") #Action 3

# Spark is lazy
# Each action can cause spark to execute the lineage required for that action

# Caching

# Persist

# filtered_df.persist(StorageLevel.MEMORY_AND_DISk)
# filtered_df.persist(StorageLevel.MEMORY_ONLY)
# filtered_df.persist(StorageLevel.DISK_ONLY)


# Unpersist
# filtered_df.unpersist()



# When does caching actually help?
# cache -> performance improvement

# cache -> When the cost of recomputing the data is greater thatn the cost of storing and retrieving it

# Scenario 2 - Caching is unnecessary

# reviews = spark.read.parquet("reviews")
# filtered_review = reviews.filter(reviews.rating > 3)

# filtered_review.cache()

# filtered_review.count() #Action - 1 | If we never use the result again, caching doesn't provide much benefits

# Scenario 3 - > When data is enormous
# Memory pressure -> Disk spills -> Potential OOM(Out of Memory issues) issues 


# Cache decision Framework
# temp = """

# Ask 4 questions:
# 1. Will I reuse this DataFrame -> If no, then don't cache

# 2. Is recomputation expensive -> If no, caching might not help

# 3. Is the cached data reasonably sized (Size good enough to get stored without OOM issues) -> If no, be careful

# 4. Is the data reused across multiple actions -> If yes, caching
# """

# types_of_plans = """

# 1. Parsed Logical Plan : What spark understood from our code

# 2. Analysed Logical Plan: Spark resolves -> Column, tables, data types, references

# 3. Optimised Logical Plan : The plan might be reagrranged or simplified safely wherever possible

# 4. Physical Plan: It describes how spark will actually execute operations

# """

# # Avoid unnecessary Shuffle
# operation_require_shuffle = """
#     groupBy()
#     join()
#     distinct()
#     orderBy()
#     repartition()
# """
# # Unneccesary shuffle
# df.repartition(1000)
# df.groupBy("city")

# # unneccesary shuffle
# df.distinct()

# df.dropDuplicates("customer_id")

# # Optimisation -> Broadcast