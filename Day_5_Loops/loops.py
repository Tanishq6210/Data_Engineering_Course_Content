
# # for num in range (10):
# #     if num == 5 or num == 7 or num == 9:
# #         continue
    
    
# #     print(num)
# #     print("Hello")
# #     print("Welcome to Python programming.")

# # print("After loop")

# # for num in range (5, 10):
# #     print(num)

# # for num in range (0, 10, 1):
# #     print(num)


# # correct_pass = "abc123"
# # while True:
# #     user_pass = input("Enter password: ")
# #     if user_pass == correct_pass:
# #         print("Access granted.")
# #         break
# #     else:
# #         print("Incorrect password. Try again.")

# # num = 1
# # while num < 10:
# #     print(num)
# #     num += 1


# # days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# # for day in days:
# #     if day == "Saturday" or day == "Sunday":
# #         print(day, "- It's the weekend!")
# #         continue

# #     print(day, "- It's a weekday.")
# #     print("Let's get to work!")

# # name = "Vinay"

# # for ch in name:
# #     if ch == "z":
# #         print("Found 'z' in the name!")
# #         break
# # else:
# #     print(f"'z' not found in the {name}")


# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# # days[1] = days[1].replace("e", "d")

# # e_alphabet_count_total = 0
# # for day in days: #Monday
# #     print(f"Processing day: {day}")

# #     e_alphabet_count_in_a_day = 0
# #     for ch in day:
# #         if ch == "e":
# #             e_alphabet_count_in_a_day += 1
# #             ch = 'd'
    
# #     # print(f"Count of 'e' in {day}: {e_alphabet_count_in_a_day}")
# #     e_alphabet_count_total += e_alphabet_count_in_a_day

# # print(f"Total count of 'e' in the days of the week: {e_alphabet_count_total}")

# # print(days)
# ch = 'd'


# name = "Ayush"
# # print(f"Length of the name: {len(name)}")

# for ch in name:
#     print(f"Character {ch}")












# # for i in range(5):










# # name = "Vinay"
# # is_found = False

# # for ch in name:
# #     if ch == "z":
# #         is_found = True
    
# # if is_found:
# #     print("Found 'z' in the name!")
# # else:
# #     print(f"'z' not found in the {name}")



# n = 5

# # *
# # **
# # ***
# # ****
# # *****

# print("Tanishq")
# print("Tyagi")



while(True):
    print("Welcome to the string analyzer!")
    print("Please enter a string to analyze, or exit to exit the program.")
    input_str = input("Enter a string:")
    if input_str.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break
    
    while(True):
        print("Enter which count you want to find (vowels/consonants/digits): ")
        print("Press 1: for vowels")
        print("Press 2: for consonants")
        print("Press 3: for digits")
        print("Press 4: to enter new string")
        count_fun = input("Enter your choice: ")
        if count_fun == "1":
            count = 0
            for char in input_str:
                if char.lower() in "aeiou":
                    count += 1
            print(f"Number of vowels: {count}")
        elif count_fun == "2":
            count = 0
            for char in input_str:
                if char.isalpha() and char.lower() not in "aeiou":
                    count += 1
            print(f"Number of consonants: {count}")
        elif count_fun == "3":
            count = 0
            for char in input_str:
                if char.isdigit():
                    count += 1
            print(f"Number of digits: {count}")
        elif count_fun == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")













            