# *args -> It is a function that allows or accept multiple positional arguments

def add(*values):
    sum = 0
    for value in values:
        sum += value
    return sum


add(1,2)
add(4,5,6,7)
print(add(6,66,7,8,9))

# **kwargs -> It is a function that accepts multiple keyword arguments
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

    # print(kwargs)

student_info(name = "Tanishq", roll_no = 123, email = "abc@gmail.com", mobile_number = 50989058, isIndian = True)


# Using *args, **kwargs together

def demo(*tuple_values, **dictionary_values):
    print(tuple_values)
    print(dictionary_values)

demo(1,2,3,4,5, name = "Tanishq", last_name = "Tyagi")

# def demo_2(**kwargs, *args):
#     print(args)
#     print(kwargs)

# demo_2(name = "Tansihq", last_name = "Tyagi", 1, 2, 3)


# Lambda Function - It is a small anonymous function
# name - square
# def square(x):
#     return x*x

def square(x):
    return x*x



print((lambda x : x*x)(4))

# Syntax of a lambda function -> 
# lambda arguments : expression

# Multiple arguments in a lambda function
calculate = lambda a, b : print(f'{a + b}')
print(calculate(2, 3))



# Map function
# flow of a map function -> item from iterable -> function -> result | Syntax -> map(function, iterable)
marks_list = [90, 85, 80, 50]

# Give 4 grace marks to all the students
def add_grace_marks(marks_list):
    for i in range(len(marks_list)):
        marks_list[i] = marks_list[i] + 5
    
    return marks_list


def add_5(num):
    return num + 5

names_list = ["taniSHQ" ,'ayUSH', 'MOksh']
updated_marks_list = map(add_5, marks_list)


print(list(updated_marks_list))
print(tuple(updated_marks_list))


# Filter function | Function returned True -> Keep, if False -> Remove | Syntax -> filter(function, iterable)

def isGreaterThanEqualsTo80(num):
    return num >= 80

marks_greater_than_80_list = filter(
    lambda num: num >= 80,
    marks_list
)

def find_average(marks_list):
    return sum(marks_list) / len(marks_list)



print(list(marks_greater_than_80_list))