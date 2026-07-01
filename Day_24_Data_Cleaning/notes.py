# Part 1 - Why Data Cleaning Matters   
# Part 2 - Handling Missing Values             
# Part 3 - Removing Duplicates                 
# Part 4 - Renaming Columns                    
# Part 5 - Changing Data Types                 
# Part 6 - String Operations                   
# Part 7 - Feature Engineering Introduction    
# Part 8 - Practical Dataset Cleaning Activity 

# Dirty Data
# 1. Missing values
# 2. Duplicate rows
# 3. Wrong data types
# 4. Messy text 
# 5. Inconsistent formatting

# Data cleaning pipeling -> Raw data -> Missing values -> Duplicates -> Wrong formats -> Standardization

# Part 2 - Handling Missing Values
# isnull() -> Checks whether every value is missing or not : return True or False

import pandas as pd 
import numpy as np

data = {
    " Student Name ": ["Rahul", "Sneha ", "AMAN", "rahul", None, "Priya"],
    "Age": [24, np.nan, 25, 22, 24, np.nan],
    "Marks": [85, 90, np.nan, 85, 78, 95],
    "City": [" delhi", "MUMBAI", "Delhi ", " delhi", " pune ", "CHENNAI"],
    "Department": ["IT", "HR", "IT", "IT", "Finance", "HR"],
    "Graduate": [True, False, True, True, False, True]
}

df = pd.DataFrame(data)

# Detecting missing values
# print(df.isnull().sum())

# Removing missing values - dropna() -> Delete rows with missing values
# print(df.dropna(axis=0)) #axis = 0 -> dropping rows, axis = 1 -> dropping columns

# Filling Missing Values -> fillna() -> Instead of deleting data, we replace missing values t

df = df.fillna(0)
print(df.info())
# print(type(df.iloc[4,0]))

df["Age"].fillna(df["Age"].mean())
df["Age"].fillna(df["Age"].median())

# What are duplicate records -> Those records in which all the values are same
# Check if duplicate exists -> duplicated() - True or False

print(df.duplicated())

# Remove duplicates -> drop_duplicates()
df = df.drop_duplicates()


# Renaming Columns
df = df.rename(columns = {" Student Name ": "student_name", "Age": "age"})

print(df)


# Changing Data Types -> astype() -> Converts the existing data type of column to another
df["age"] = df["age"].astype(int)

# print(df["student_name"])
# # String Operations
df["student_name"] = df["student_name"].str.title()
df["student_name"] = df["student_name"].str.strip() # Removes leading and trailing spaces
# df = df["Name"].str.replace(" ", "_")

print(df)