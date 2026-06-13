name = "Tanishq Tyagi"
# T + a + n + i + s + h + q + _ + T + y + a + g + i

name = "k" + name[1:]
print(name)

# Cleaning Methods
# Method 1 - strip() - Removes the spaces in the left and right
name_of_john = "       JOHN DOE      "
print(name_of_john)
stripped_name_of_john = name_of_john.strip()
print(stripped_name_of_john)

name2 = "jaNe SmiTH"
name3 = "Jane SMIth"
name_of_john = "      JOHN DOE      "


# Method 2 - lstrip()- Remove the spaces in the left
name = "manAV sood sinha singh   manav manav  "
print(len(name.lstrip()))

# Method 3 - rstrip() - Remove the spaces in the right side
print(len(name.rstrip()))

# Method 4 - upper() - To convert the entire string to upper case
print(name.strip().upper())

# Method 5 - lower() - To convert the entire string value to lower
print(name.strip().upper())

# Method 6 - title() - To conver the string to camelCase
print(name.strip().title())


# Searching and Replacing
#Method 1 - find() - This is used to find the index of the word being searched inside the string

if name.strip().lower().find("manav") == -1:
    print("not found!")
else:
    print("Found")

# Method 2 - Replace - To replace a string value with other value
# name = name.lower().replace("manav", "Ayush")
# print(name)

# Method 3 - count()
count_of_manav = name.lower().count("manav")
print(count_of_manav)


name = "    T a n i s h q T y a g i    "
print(name.lower().strip().replace(" ",""))

# Method 4 - startsWith() - If the given string starts with the other string to be checked

if name.lower().replace(" ","").startswith("Tan".lower()):
    print("Yes! name starts with Tan!")
else:
    print("No, name does not starts with Tan!")    
    
# Method 5 - endsWith()
email_id = "tanishq@gmail.com"
if email_id.endswith(".com") and email_id.find("@") != -1:
    print("valid email!")


# Part 4 - Parsing Techniques
# Method 1 - split() - Splits the string into multiple values from delimitor
fruits = "apple,banana,chiku,mango"
fruits_list = fruits.split(",,")
print(fruits_list)


# Method 2 - .join()
name = ["Tanishq", "Tyagi"]
print("$".join(name))

num_list = [1, 2, 3]
# print(",".join(num_list))


sentence = "i am not so awesome."
print(sentence.capitalize())
print(sentence.title())



sentence = "Tanishq"


print(sentence[2:5])


print(sentence.find("") != -1)
print("" in sentence)
