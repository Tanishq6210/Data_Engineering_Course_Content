# Error -> a problem that prevents the programm from running correctly
# Type of Error -> Syntax error

if 10 > 5:
    print("Hello World!")

# Exception -> Runtime Errors | Definition -> These are the errors that come during the execution of the programm
print("Hey, I'm the second statement!")

num = 10
# print(num / 0)

print("Programm Finished!")

# Common built in Exceptions
# 1. Value Error
val = int("90")
print(type(val))

# 2. Type Error
# print("10" + 5)

# 3. FileNotFoundError
# with open("abc.txt", "r") as file:
#     val = int(input("Enter a valid integer: "))
#     data = file.read()
#     print("hi")

# 4. ZeroDivision Error
# print(10 / 0)
# select * from table where table.column_name = 'abc'
# try-except block -> Foundation of exception handling
def validate_age(age):
    if age > 0 and age < 150:
        return True
    
    # To throw the error as per the usecase
    raise ValueError("Invalid age, Age should be in between 0 to 150")

age = 0
while True:
    try:
        age = int(input("Enter your age: "))
        # validate_age(age)
    except ZeroDivisionError:
        print("0 is an invalid input! Give some other number :)")
    except ValueError as e:
        print("Invalid SQL!")
    else: #It will be executed, when no exception was produced in the try block
        print(f'Your age is:  {age}')
    finally: #This block will always execute, irrespective of error was thrown or not by the try block
        print("Programm Finished!")

