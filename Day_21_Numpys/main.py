# Part 0 - Recap & Quiz
# Part 1 - Introduction & Why NumPy?
# Part 2 - NumPy Arrays
# Part 3 - Operations & Broadcasting
# Part 4 - Hands-on Practical
# Part 5 - Performance Comparison & Wrap-up

# NumPy - > Numerical Python
# Usecase ->
# Fast numerical computations
# Scientific computing
# Matrix operations
# Machine Learning
# Data analysis


# CSV contating salary of 5 million employees
# List

# Can I perform any operation on all the salaries - Yes

# Will that be fast? -> No

# Limitations of Python Lists
# Is List -> Heterogenous / Homogenous
my_list = ["Tanishq", 1, 2, 3, 5, True, 5.0]

# 1. Object overhead
# list -> references of objects -> object -> value
# 2. Sequential processing of elements

# Why NumPys
# No object overhead -> Continuous memory allocation, homogenous data only
# Heavy computations happen in optmized C language code


# NumPy Syntax
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(type(arr))
# ndarray -> N-Dimensional Array

arr_dim = np.array([[10,20,30],[40,50,60]])


print(arr_dim.shape) #no.of rows x no. of columns
print(arr_dim.ndim) #no. of dimension
print(arr_dim.size) 
print(arr_dim.dtype)

# How to create arrays
#1. By giving list as input
#2. ones
#3. zeroes
#4. arrange

array = np.arange(10)
array = np.arange(2, 10, 2)
print(array)

zero_list = np.zeros(5, dtype=int)
print(zero_list)
print(zero_list.dtype)

one_list = np.ones(5, dtype=int)
print(one_list)
print(one_list.dtype)

# Element wise Arithmetic
list_a = [1, 2, 3]
list_b = [1, 2, 3]

numpy_list_a = np.array(list_a)
numpy_list_b = np.array(list_b)
print(list_a + list_b)
print(numpy_list_a + numpy_list_b)
print(numpy_list_a - numpy_list_b)
print(numpy_list_a * numpy_list_b)
print(numpy_list_a / numpy_list_b)

# Aggregate Functions
max_num = numpy_list_a.max()
min_num = numpy_list_a.min()
mean_num = numpy_list_a.mean()
sum_num = numpy_list_a.sum()

print(f"max: {max_num}\nmin: {min_num}\nmean: {mean_num}\nsum: {sum_num}")


# Vectorization & Broadcasting
marks = np.array([90, 85, 80, 75])
print(marks + 5)


# Time difference between list and numpy arrays
import time

numbers = list(range(1_000_000))
aray = np.arange(1_000_000)

# List Timme
result = []
start = time.time()
for x in numbers:
    result.append(x * 2)
list_time = time.time() - start


# Numpy Time
start = time.time()
result = aray * 2
numpy_time = time.time() - start

print(f"List time: {list_time:.5f} seconds")
print(f"Numpy time: {numpy_time:.5f} seconds")