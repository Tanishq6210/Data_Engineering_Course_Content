import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, trim, upper

spark = SparkSession.builder.appName("EmployeeExpenseCleaning").getOrCreate()


data = [
    ("EXP001", "E101", "Aarav Mehta", "28", "Engineering", "Bangalore", "1250.50", "2", "Approved", "2026-08-01", "true", "Client meeting"),
    ("EXP002", "E102", "Isha Sharma", "31", "engineering", "Delhi", "850.00", "1", "Approved", "2026-08-02", "true", "Travel expense"),
    ("EXP003", "E103", "Kabir Singh", "26", "ENGINEERING", " Bangalore ", "450.75", "3", "Pending", "2026-08-03", "true", "Office supplies"),
    ("EXP004", "E104", "Ananya Gupta", "35", "Finance", "Mumbai", "2200.00", "2", "Approved", "2026-08-03", "true", "Business travel"),
    ("EXP005", "E105", "Rohan Verma", "-4", "HR", "Delhi", "750.00", "1", "Approved", "2026-08-04", "true", "Invalid age"),
    ("EXP006", "E106", "Diya Kapoor", "29", "Marketing", "Mumbai", "invalid", "2", "Pending", "2026-08-05", "true", "Invalid amount"),
    ("EXP007", "E107", "Arjun Malhotra", "42", "Finance", "Delhi", "", "1", "Approved", "2026-08-05", "true", "Missing amount"),
    ("EXP008", "E108", "Meera Joshi", "27", "HR", "DELHI", "1200.00", "", "Approved", "2026-08-06", "true", "Missing quantity"),
    ("EXP009", "E109", "Aditya Rao", "", "Marketing", "Mumbai", "950.50", "2", "Approved", "2026-08-07", "true", "Missing age"),
    ("EXP010", "E110", "Sneha Iyer", "33", "finance", "mumbai", "1750.00", "2", "Rejected", "2026-08-07", "false", "Rejected claim"),
    ("EXP011", "E111", "Vivek Nair", "39", "Engineering", "Bangalore", "500.00", "-2", "Approved", "2026-08-08", "true", "Invalid quantity"),
    ("EXP012", "E112", "Pooja Shah", "24", "Marketing", "Delhi", "-300.00", "1", "Approved", "2026-08-08", "true", "Negative amount"),
    ("EXP013", "E113", "Kunal Agarwal", "45", " HR ", " Delhi ", "1350.00", "2", "Approved", "2026-08-09", "true", "Formatting issue"),
    ("EXP014", "E114", "Nisha Bansal", "17", "Finance", "Mumbai", "2100.00", "1", "Approved", "2026-08-09", "true", "Underage employee"),
    ("EXP015", "E115", "Manav Sethi", "52", "Engineering", "Bangalore", "800.00", "4", "Approved", "2026-08-10", "true", "Team event"),
    ("EXP016", "E116", "Tanya Khanna", "30", "MARKETING", " DELHI ", "invalid", "1", "Pending", "2026-08-10", "true", "Invalid amount"),
    ("EXP017", "E117", "Yash Tandon", "37", "Finance", "Mumbai", "1450.00", "3", "Approved", "2026-08-11", "true", "Travel reimbursement"),
    ("EXP018", "E118", "Ritika Sood", "25", "marketing", "Delhi", "900.00", "", "Approved", "2026-08-11", "true", "Missing quantity"),
    ("EXP019", "E119", "Sahil Jain", "41", "Engineering", " Bangalore ", "1100.00", "2", "Approved", "2026-08-12", "true", "Client visit"),
    ("EXP020", "E120", "Aditi Mishra", "29", "Finance", "Delhi", "600.00", "1", "Approved", "2026-08-12", "false", "Inactive employee")
]


columns = [
    "expense_id",
    "employee_id",
    "employee_name",
    "age",
    "department",
    "location",
    "expense_amount",
    "quantity",
    "status",
    "expense_date",
    "is_active",
    "internal_comment"
]


df = spark.createDataFrame(data, columns)

df.show(truncate=False)

# DataFrame Transformations
# 1. select() - it is used when you want to choose particular columns from a dataframe

df.select("expense_id", "employee_name").show()

# 2. alias() -> It allows us to give a column or expression a temporary / output name
df.select(df.department.alias("employee_department")).show()

df.select(col("department").alias("employee_department")).show()

# 3. filter() / where() - It is used to keep only rows satisfying a condition | No functional difference in filter() and where()
df.filter(df.is_active == True).show()
df.where(col("is_active") == True).show()

# 3.1 Multiple filter conditions - & - And, | - Or, ~ - Not
df.filter(
    (col("age") >= 18) & (col("is_active") == True) & (col("is_active") == True) & (col("is_active") == True) & (col("is_active") == True)
)

df.filter(~col("is_active") == True)

# 4 withColumn() - 
# 4.1 - Create a new column
# 4.2 - Modify an existing column

df = df.withColumn("expense_amount", col("expense_amount") * 2)

# Type Conversion / cast()
df.withColumn("age", col("age").cast(IntegerType))

# Null values handling

# Detecting NULL values
df.filter(col("age").isNull()).show()

df.filter(col("age").isNotNull()).show()

df.select(
    count(where(col("age").isNull(), True))
)

# Never fill missing values blindly. Choose a replacement based on the requirement
# Fill null values
df.na.fill({"discount_percentage": 0})

# Drop null values
df.na.drop(subset=["price", "quantity"])

# Drop columns
df.drop("abc", "xyz")

# Data Quality - It means how trustworthy and usabel the data is for its intended purpose
# 1. Completeness - are required values are present or not
# 2. Accuracy - Are the values corrrect 
# 3. Consistency - Are the values consistent across the dataset
# 4. Validity - Does the value follow expected rule
# 5. Uniqueness - Are the values unique

df = df.withColumn("city", trim(upper(col("city"))))