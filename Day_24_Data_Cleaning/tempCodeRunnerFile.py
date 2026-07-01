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

df = {
    " Student Name ": ["Rahul", "Sneha ", "AMAN", "rahul", None, "Priya"],
    "Age": [24, np.nan, 25, 22, 24, np.nan],
    "Marks": [85, 90, np.nan, 85, 78, 95],
    "City": [" delhi", "MUMBAI", "Delhi ", " delhi", " pune ", "CHENNAI"],
    "Department": ["IT", "HR", "IT", "IT", "Finance", "HR"]
}

print(np.nan + 3)