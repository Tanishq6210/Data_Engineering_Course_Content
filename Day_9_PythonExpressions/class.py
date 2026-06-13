#for loop
list_num = []
for i in range(1, 11):
    list_num.append(i)
# print(list_num)



list_nums = [1,2, 3, 4, 5]
for i in list_nums:
    list_num.append(i*2)

#List - Comprehension
list_num = [i+2 for i in list_nums]
print(list_num)

squares_num = [x*x for x in list_nums]

#Syntax
# [expression for item in iterable]


#Conditional Filtering
for i in range(1, 11):
    if i%2 == 0:
        list_num.append(i)

even_list_num = [i for i in range(1, 11) if i%2 == 0]
print(even_list_num)

#Syntax
#[expression for item in iterable if condition]


#Dictionary Comprehensions
# {
#     key:value
#     for item in iterable
# }

# squares_dict = {}
# for i in range(1, 2):
#     squares_dict[i] = i*i
# print(squares_dict)

#Dictionary Comprehension
squares_dict = {i:i*i for i in range(1, 6)}
print(squares_dict)

employees_dict = {
    "John": 55000,
    "Jane": 60000,
    "Jane": 65000,
}

print(employees_dict)

updated_employees_dict = {name: salary*1.1 for name, salary in employees_dict.items()}
print(updated_employees_dict)


# Function to check if a string starts with "A" or "J"
names = ["JRonak", "Khushboo", "ATanishq"]
names_starting_with_a_or_j = [name for name in names if (name.startswith("A") or name.startswith("J"))]

names_starting_with_a_or_j = [name for name in names if (name[0] == 'A' or name[0] == 'J')]
print(names_starting_with_a_or_j)


# Nested Comprehensions
matrix = [
    [1, 2, 3],
    [4, 5],
    [7, 8, 9]
]

# Tradition for loop
for row in matrix:
    if len(row) == 3:
        for cell_value in row:
            if cell_value % 2 == 0:
                print(cell_value)

# Syntax for nested comprehensions
# [expression for item1 in iterable1 for item2 in iterable2]
result = [cell_value for row in matrix for cell_value in row if cell_value % 2 == 0]
print(result)

# Print multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(table)

result = [
(i, j)
for i in range(1,4)
for j in range(i,4)
if (i*j) % 2 == 0
]

print(result)


even_row = [cell_value for row in matrix if len(row) == 3 for cell_value in row]

print(even_row)

# [expression_if_true if condition else expression_if_false for item in iterable]