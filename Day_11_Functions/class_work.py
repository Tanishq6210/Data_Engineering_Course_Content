# Functions -> Reusable block of code designed to perform a specific task.

# Define a function
def add(num1, num2):

    sum = num1 + num2
    print(f'{num1} + {num2} = {sum}')

    return sum

a = 10
b = 20

# print(num1 + num2) #Addition
add(a, b)

# Multiple task in middle (200 line)

num1 = 4
num2 = 6
# print(num1 + num2) #Addition
add(4, 6)


# Multiple task in middle (300 line)

num1 = 23
num2 = 45

# print(num1 + num2) #Addition
add(num1, num2)
# subtract(num1, num2)
# multiply(num1, num2)
# divide(num1, num2)
# power(num1, num2)


# Multiple task in middle


# Benefits 
# 1. Code reusability - To use the same logic again and again
# 2. Modularity - To divide the programm into multiple small modules for easy debugging and to increase code readability
# 3. DRY principle

# Parameters and Arguments

def print_list_elements(list_data):
    for data in list_data:
        print(data)

    print("Printed list elements!")

names = ["Shachi", "Mourya", "Vibhore"]

# Positional arguments
print_list_elements(names)

# Keyword arguments
def print_name_age(name, age):
    print(f'Name is {name}, my age is {age}')

print_name_age(age = 4, name = "Tanishq")

# Default Parameters
def greet_user(name="User"):
    print(f'Welcome aboard! {name}')

greet_user()

print("--------------")
# return keyword
def sum_of_list_elements(list_of_nums):
    sum = 0
    for num in list_of_nums:
        sum += num

    print("hello world")
    return sum


def find_avg(sum, n):
    return sum / n

def calculate_sum_and_avg(list_of_nums):
    sum = sum_of_list_elements(list_of_nums)
    avg = find_avg(sum, len(list_of_nums))

    return sum, avg

list_of_nums = [1, 2, 3, 4, 5, 6]
sum, avg = calculate_sum_and_avg(list_of_nums) #unpacking

print(f"For list: {list_of_nums}, sum = {sum}, avg = {avg}")

# Scope of a variable

# Global variable
a = 10

def print_a():
    c = 10 #Local variable
    print(f"Value of a is: {c}")

def print_c():
    # print(f'Value of b is {c}')
    print()

print_a()
print_c()
# print(c)


# Scope Resolution - LEGB (Local -> Enclosing -> Global -> Builtin)

name = "Global Tanishq"
def outer_function():
    message = "Hello from the enclosing scope!" #Enclosing variable
    # name = "Enclosing Tanishq"

    def inner_function():
        # name = "Inner Tanishq" #Local variable
        print(f'name: {name}, message = {message}')

    inner_function()

outer_function()

"Tanishq".split(sep = ",")