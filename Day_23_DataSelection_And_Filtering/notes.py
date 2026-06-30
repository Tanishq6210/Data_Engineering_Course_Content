# Data Selection & Filtering in dataframe

import pandas as pd

employees = pd.DataFrame({
    "Name": ["Vibhore", "Manav", "Aditi", "Sachi", "Ayush", "Manendar"],
    "Department": ["IT", "IT", "Finance", "HR", "HR", "IT"],
    "Age": [24, 25, 26, 27, 28, 20]
}, index = [101, 101, 103, 104, 105, 106])

# Column filtering

# print(employees["Age"])
# print(employees[["EMP_ID", "Age"]])
# print(type(employees[["EMP_ID", "Age"]]))

print(employees)

# Row filtering
# 2 ways to do the row level filtering -
# 1. loc
# 2. iloc

# LOC[] -> Label Based selection (Find rows using their labels)
# print(employees.loc[101]) # Fetching single row
# print(employees.loc[[101, 106]]) #Fetching multiple row
# print(employees.loc[101:106]) #Fetching row range (It will include the last label as well)

# Selection rows and columns together
# print(employees.loc[102:104, ["Name", "Age"]])

# iloc[] -> Position based selection (Find row using their position)
# print(employees.iloc[4])
# print(employees.iloc[[0,5]])
print(employees.iloc[0:2:2]) #It will exclude the last mentioned position of the range)

# Boolean Indexing - Filtering of Dataframe

# For multiple conditions - parenthesis is mandatory
# print(employees[
#     ~(employees["Department"] == "IT")
#     ])

# Comparison operators -> >, <, >=, <=, ==, !=
# Logical operators -> &, |, ~

# Sorting data
# Sort a single column
# print(employees.sort_values("Age", ascending = False))

# Multiple values sorting
# print(employees.sort_values(
#     ["Department", "Age"], 
#     ascending = [True, False])
#     )