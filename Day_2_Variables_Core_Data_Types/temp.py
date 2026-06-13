# name = input("Enter your name: ")
# age = int(input())
# marks = input("Enter your marks: ")

# print("Hello World!")
# print("Hello, ", name)
# print("Hello " + name)
# print(f"{name} is my name is")

# print(f"Type of age variable: {type(age)}")
# print("Type of age variable:", type(age))

# print(f"Type of age variable: {type(age)}")
# multiplied_by_2 = age * 2
# print(f"Your age is: {multiplied_by_2}")
# print(name,"how are u")



a = 5
b = 2

# Arithmetic Operations
sum = a + b
diff = a - b
product = a * b
quotient = a / b
remainder = a % b
# print(f"Sum: {sum}, Difference: {diff}, Product: {product}, Quotient: {quotient}, Remainder: {remainder}")



int_part_division = a // b
# print(f"Floor Division: {int_part_division}")

power = a ** b
# print(f"{a} to the power {b}: {power}")


a = 5
b = 5

# Comparison Operators
is_equal = a == b
is_not_equal = a != b
is_greater = a > b
is_greater_equal = a >= b
is_less = a < b
is_less_equal = a <= b

# print(f"Is {a} equal to {b}? {is_equal}")
# print(f"Is {a} not equal to {b}? {is_not_equal}")
# print(f"Is {a} greater than {b}? {is_greater}")
# print(f"Is {a} greater than or equal to {b}? {is_greater_equal}")
# print(f"Is {a} less than {b}? {is_less}")
# print(f"Is {a} less than or equal to {b}? {is_less_equal}")

c = True and True
# print(c)
c = True and False
# print(c)
c = False and True
# print(c)
c = False and False
# print(c)

standard = 7
grade = "A"
age = 12
name = "Manav"
phone_num = 123

# print(standard == 7 and grade == "B" and age == 12 and name == "Manav")
# print(False and age == 12 and name == "Manav")
# print(False and name == "Manav")

# d = True or True
# print(d)
# d = True or False
# print(d)
# d = False or True
# print(d)
# d = False or False
# print(d)

# print(phone_num != 123 or name == "Manav" or age != 12)

# print((phone_num == 123 or name != "Manav") and age != 12)

# not -> !
# Precedence: () > not > and > or
is_logged_in = True
is_logged_in = (not is_logged_in)

# print(is_logged_in) #
# print(not is_logged_in) #

# print(is_logged_in)


age = 2
# print(age)
age = 3 * age
age = age + 1
age = age - 10
age = age / 2
age = age ** 2
age = age % 3
# print(age)

#Short hand notations
age = 2
# print(age)
age *= 3
age += 1
age -= 10
age /= 2
age **= 2
age %= 3
# print(age)



#BODMAS -> Brackets, Orders, Division, Multiplication, Addition, Subtraction
result = 2 + 3 * 4
# print(result)

# ()
# **
# *, /, //, %
# +, -
# Comparison (==, !=, >, <, >=, <=)
# not
# and
# or


abc = bool(int(input()))
print(abc)

num1 = int(input(f"enter number number1: "))
num2 = int(input(f"enter number number2: "))