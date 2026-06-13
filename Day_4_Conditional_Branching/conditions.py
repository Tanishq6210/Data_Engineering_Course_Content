# age = int(input("Enter your age: "))


# # if age > 18:
# #     print("Voting allowed!")
# # else:
# #     print("Voting not allowed!")


# # is_logged_in = False

# # if is_logged_in:
# #     print("Watch the content.")
# # else:
# #     print("Please sign up or log in to continue.")
# #     print("Redirecting to login page...")
# #     print("Login successful!")

# #     a = 1 + 1
    

# salary = 80000
# working_hours = 30
# if (salary > 50000 or working_hours > 40):
#     print("You are eligible for a bonus!")
# else:
#     print("You are not eligible for a bonus.")

# print("Program ended.")





# rating = 5

# if rating == 5:
#     print("50000 bonus")
# elif rating == 4:
#     print("40000 bonus")
# elif rating == 3:
#     print("30000 bonus")
# elif rating == 2 or rating == 1:
#     print("No Bonus")

# age = 40
# degree = "Bsc"
# branch = "CS"

# if age > 24:
#     if degree == "B.Tech":
#         if branch == "CS":
#             print("You are eligible for the Data Engineer.")
#         else:
#             print("You do not have the required branch.")
#     else:
#         print("You do not have the required degree.")
# else:
#     print("You are not old enough for the job.")



# age = int(input("Enter your age: "))

# age = 40

# if age > 18:
#     status = "Voting allowed!"
# else:
#     status = "Voting not allowed!"


# status = "Voting allowed!" if age > 18 else "Voting not allowed!"

# # value_if_true if condition else value_if_false
# print(status)

# Q 1:
# age and rating
#Branching age > 24 and rating > 4 -> "Best employee"
#age > 24 and rating > 3 -> "Good employee"
#age > 24 and rating > 2 -> "Average employee"
#age < 1 -> "You are not born yet!"


# 2
#current_balance -> 10000
#amount_to_be_withdrawn -> User input
# current_balance = int(input("Enter your current balance: "))
# amount_to_be_withdrawn = int(input("Enter the amount you want to withdraw: "))

# if amount_to_be_withdrawn > current_balance:
#     print("Insufficient funds. Withdrawal denied.")
# else:
#     print("Withdrawal successful. Please take your cash.")

# Q3 
# take 3 integer inputs from the user -> print the largest and the smallest
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# largest = num1
# if num1 > num2 and num1 > num3:
#     largest = num1
# elif num2 > num1 and num2 > num3:
#     largest = num2
# else:
#     largest = num3

# smallest = num1
# if num1 < num2 and num1 < num3:
#     smallest = num1
# elif num2 < num1 and num2 < num3:
#     smallest = num2
# else:
#     smallest = num3

# print("The largest number is:", largest)
# print("The smallest number is:", smallest)

# print("The largest number is:", largest)


# x = 5 if x == 5 or 6: print(“X..”) else: print(“x.fd”)
                                               
x = 5

if x != 5 or x==6:
    print("Hii")
else:
    print("Hello")
                                               
                                               
# Q4
#Grade classification programm


#switch case in python
# age = 40
# match age:
#     case 18:
#         print("You are 18 years old.")
#     case 40:
#         print("You are 40 years old.")
#     case _:
#         print("Age not matched.")

# if age == 18:
#     print("You are 18 years old.")
# elif age == 40:
#     print("You are 40 years old.")
# else:
#     print("Age not matched.")