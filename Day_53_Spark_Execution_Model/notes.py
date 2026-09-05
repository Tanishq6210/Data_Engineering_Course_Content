from pyspark.sql import SparkSession    
data = [
    ("Tanishq", "Delhi", 1000),
    ("Rahul", "Mumbai", 2000),
    ("Priya", "Delhi", 1500),
    ("Amit", "Mumbai", 3000)
]

spark = (
    SparkSession.builder.appName("Spark Architecture")
         .master("local[*]")
         .getOrCreate()
)


df = spark.createDataFrame(
    data,
    ["name", "city", "amount"]
)

#Stage 1
# NT
df2 = df.filter(df.amount > 1500) # Transformation 1
df3 = df2.select("name", "city") # Transformation 2
df4 = df3.withColumn("tax", df2.amount * 0.1) #Transformation 3

# Stage 2 - Wide Transformation
df4.groupby("city")
df4.having(df4.tax > 200)

# Stage 3 - Wide Transformation
df4.groupBy()

# Actions
df.show() #Action 1
df.count() #Action 2
df.collect() #Action 3
df.first() #Action 4


df.write.format("csv").save("output.csv")