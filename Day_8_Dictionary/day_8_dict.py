# Dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed.

# Examples
my_dict = {"name": "Dorya", "age": 20}

my_list = [1, 2, 3, 4]
contacts = {
    "Dorya" : 1234567890,
    (1, 2) : 9876543210,
    1 : "One"
}

# Accessing values in a dictionary ex, dictionary_name[key]
print(contacts["Dorya"])
print(contacts[(1,2)])
print(contacts[1])

print(contacts.get("Dorya"))

# Difference between [] and .get() method

# [] -> If the key is not present in the dictionary, it will raise a KeyError
# print(contacts["Tanishq"])

# .get() -> If the key is not present in the dictionary, it will return None
print(contacts.get("Tanishq"))


# Accessing all keys, values, and key-value pairs in a dictionary
print("-------------------------------------")
for key, value in contacts.items():
    print(f"Key: {key}, Value: {value}")


# Adding a new key-value pair to the dictionary
contacts["Rohit"] = 1122334455
print(contacts)
contacts[(1, 2)] = 1111111111


students_dict = {
    1: {
        "name": {
            "first_name": "Dorya",
            "last_name": "Sharma"
        },
        "marks": {
            "Math": 90,
            "Science": 95,
            "English": 85
        }
    },
    2: {
        "name": "Tanishq", 
        "marks": {
            "Math": 80,
            "Science": 85,
            "English": 90
        }
    }
}
print(students_dict[1]["marks"]["Science"])


print("--------------------------------------")
# How to iterate a nested dictionary?
iteration = 1
for student_id, student_info in students_dict.items(): #1, 2
    print(f'Iteration: {iteration}\n')
    print(f"Student ID: {student_id}")
    print(f"Student Name: {student_info['name']}")
    print("Marks:")

    for subject, marks in student_info["marks"].items():
        print(f"{subject}: {marks}")

    iteration += 1

for contact in contacts.items():
    print(type(contact))
    print(contact)

print(contacts.keys())
print(contacts.values())

name = "Hello"
value = 9038590285908
contacts[name] = value
print(contacts)