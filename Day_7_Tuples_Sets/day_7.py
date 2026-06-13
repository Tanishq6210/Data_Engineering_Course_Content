# numbers = 1, "Hello", True
# print(type(numbers))
# numbers_single = 1,
# print(type(numbers_single))

# Immutability
numbers_list = [1, 2, 3]
numbers_list[0] = 100

# Packing a tuple
customer = "Tanishq", 123, 100, [1, 2, 3], "Manav"

# print(customer[0])
# print(customer[1])
# print(customer[2])
# print(customer[3])
# print(customer[4])

# customer[3] = [4, 5, 6]

customer[3].append(7)

# print(customer[3])

# Unpacking a tuple
customer_name, customer_id, customer_balance, customer_list, customer_second_name = customer
# print(customer_name)
# print(customer_id)
# print(customer_balance)

# print(customer_second_name)

# Create a student tuple with the information of your choice


numbers = [1, 2, 3, 4]

numbers_tuple = (1, 2, numbers, 4)
numbers = [5, 6, 7, 8]

# print(numbers_tuple)

# Sets
student_ids = [1, 2, 3, 4, 1, 2, 3]
print(len(student_ids))
print(type(student_ids))

unique_student_ids = set(student_ids)
print(type(unique_student_ids))
print(unique_student_ids)

numbers_set = {1, 2, 3, 4, 1, 2, 3}
print(type(numbers_set))
# print(numbers_set)

student_tuples = ("Tanishq", 1, 1, 2, "Tanishq")
student_set = set(student_tuples)
print(student_set)

# .add() -> adds an element to the set
# .remove() -> removes an element from the set

student_set.add("Manav")
print(student_set)
student_set.remove("Tanishq")
print(student_set)

# [1, 2, 3, 4, 5]
print(5 in student_set)
# O(1)


# Converting set to a list
student_list = list(student_set)
print(student_list)

# Take 2 lists as input, using for loop, define 5 elements in each list, convert them to sets and perform union, intersection, difference and symmetric difference operations on them.

# While True:


numbers_set_1 = {1, 2, 3, 4}
numbers_set_2 = {3, 4, 5, 6}

numbers_set_union = numbers_set_1 | numbers_set_2
# numbers_set_3 = numbers_set_1.union(numbers_set_2)
print(type(numbers_set_union))
print(numbers_set_union)

# numbers_set_intersection = numbers_set_1 & numbers_set_2
numbers_set_intersection = numbers_set_1.intersection(numbers_set_2)
print(type(numbers_set_intersection))
print(numbers_set_intersection)


numbers_set_difference = numbers_set_2 - numbers_set_1
numbers_set_difference = numbers_set_1.difference(numbers_set_2)
print(type(numbers_set_difference))
print(numbers_set_difference)


# numbers_set_sym_diff = numbers_set_1 ^ numbers_set_2
numbers_set_sym_diff = numbers_set_1.symmetric_difference(numbers_set_2)
print(type(numbers_set_sym_diff))
print(numbers_set_sym_diff)


abc = [1, 2, 3, 4]
abc[1] = abc
print(abc)

