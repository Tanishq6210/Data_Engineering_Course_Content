# Part 0 - Recap & Quiz
# Part 1 - Why do we need pandas?
# Part 2 - Series vs DataFrame
# Part 3 - Reading Data
# Part 4 - Understanding Dataset Structure
# Part 5 - Practical 


# Flipkart - 50 million orders
order_id = [1001,     1002,      1005]
prices =   [500,      600,        700]
cities =   ["Delhi", "Mumbai", "Pune"]

# Problems
# 1. 3 different lists


# Pandas -> Excel inside python with some superpowers
# Pandas helps in organising data into tables

# Why data engineers love pandas
# Extract (CSV, Json, Excel, Database) Pandas -> cleaning -> Transformation -> Matrics -> Storing

# Numpy
# It is good for -> mathematical operations, arrays and matrices (Single data type)
# Not good for -> Different data types, cleaning, missing value


import pandas as pd
import numpy as np

arr = np.array([
    [101, 500],
    [102, 700]
])

# It helps in adding labels to the columns

df = pd.DataFrame({
    "OrderId": [101, 102],
    "Price":[500, 700]
})

# numpy -> A warehouse full of numbered boxes
# pandas -> A warehouse with labeled boxes

# Part 2 -> Series & DataFrame

# What is series? -> A one-dimensionoal labeled array
students = pd.Series(["Vibhore", "Aditi", "Manav"])
print(students)

# Flexibility -> You can give your custom index to each value
students = pd.Series(
    ["Vibhore", "Aditi", "Manav"],
    index = ["EMP101", "EMP102", "EMP103"]
)

print(students)
print(students["EMP103"])

# Dataframe -> A dataframe is a two-dimensional labeled table

df = pd.DataFrame({
    "ID": [1, 2], #series
    "Name": ["Sachi", "Ayush"], #series
    "Age": [21, 22] #series
})

# Reading data -> CSV, Excel, Json
df = pd.read_csv("data/students.csv")
# print(df)


# openpyxl -> Dependency to be installed to read a excel file
df = pd.read_excel("data/contact_responses.xlsx")
# print(df)

df = pd.read_json("data/student.json")
# print(df)

# dataset -> 1 million
# print(df.head(2))
# print(df.dtypes)
# print(type(df))

# df.info() # no. of rows, columns, names, data types, non null count, memory usage | Dataset information

# Summary Statistics
print(df[["Age", "Marks"]].describe())

def data_range(column):
    return column.max() - column.min()

df.agg(["mean", "std", data_range])


df.describe(percentiles = [0.10, 0.50, 0.80])