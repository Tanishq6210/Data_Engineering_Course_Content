# Recap & Quizz
# Introduction & Why Grouping Matters
# GroupBy + Aggregations
# Multiple Aggregations using agg()
# Merging & Joining
# Concatenation
# Mini Project Explanation

# Grouping and Joining of DataFrames

# Grouping -> Grouping of similar records together and performing some operations
# groupby() -> It works on strategy -> Split, Apply, Combine

import pandas as pd

customers = pd.DataFrame({
    "CustomerID": [101, 102, 103, 104, 105],
    "CustomerName": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Region": ["North", "South", "East", "West", "North"]
})

sales = pd.DataFrame({
    "OrderID": ["O001", "O002", "O003", "O004", "O005", "O006"],
    "CustomerID": [101,    102,    101,    103,   104,   106],
    "ProductID": ["P101", "P102", "P101", "P105", "P104", "P102"],
    "Quantity": [1, 2, 3, 2, 1, 1],
    "Sales": [55000, 40000, 15000, 6000, 12000, 20000]
})

# Grouping single column
print(customers.groupby("Region")["CustomerID"].count())

print(sales.groupby("ProductID")["Sales"].mean())

# Aggregate functions -> sum(), mean(), min(), max(), count(), median(), std()

# Grouping multiple columns
print(sales.groupby(["CustomerID", "ProductID"])["Sales"].sum())


# Multipple Aggregations using agg()
print(sales.groupby("ProductID")["Sales"].agg(["sum", "mean", "max", "min"]))


# Merging DataFrames -> To combine to or more dataframes into a single dataframe

# 1. Inner Join
# 2. Outer Join
# 3. Left Join
# 4. Right Join


# Students dataframe
students = pd.DataFrame({
    "StudentID": [101, 102, 103, 104, 105],
    "StudentName": ["Alice", "Bob", "Charlie", "David", "Eva"]
})

courses = pd.DataFrame({
    "StudentID": [101, 101, 101, 101],
    "CourseID": ["C-101", "C-202", "C-203", "C-204"],
    "CourseName": ["Math", "Science", "History", "Art"]
})

inner_join = pd.merge(
    students, courses, on="StudentID", how="inner"
)

print(inner_join)

# Left Join
print("== Left Join ==")
left_join = pd.merge(
    students,
    courses,
    on="StudentID",
    how="left"
)
print(left_join)

# Right Join
print("== Right Join ==")
right_join = pd.merge(
    students,
    courses,
    on="StudentID",
    how="right"
)

print(right_join)

# Outer Join
print("== Outer Join ==")
outer_join = pd.merge(
    students,
    courses,
    on="StudentID",
    how="outer"
)

print(outer_join)

# Concatenation
# 2 types of concatenation -> 1. Vertical 2. Horizontal

# df1 = pd.DataFrame({
#     "Name": ["Vibhore", "Krishan"],
#     "Age": [25, 30]
# })

# df2 = pd.DataFrame({
#     "Name": ["Aditi", "Pratigya"],
#     "Age": [28, 27]
# })

# # Vertical Concatenation
# result = pd.concat([df1, df2], ignore_index=True)
# print(result)


df1 = pd.DataFrame({
    "Name": ["Vibhore", "Krishan"]
})

df2 = pd.DataFrame({
    "Age": [28, 27]
}, index = [1, 2])

# Horizontal Concatenation
result = pd.concat([df1, df2], axis=1)
print(result)