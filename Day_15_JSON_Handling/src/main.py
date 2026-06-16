import json

# JSON -> Java script object notation

# swiggy_account
{
    "name": "Rohan",
    "email": "rohan.gandhi@gmail.com",
    "city": "Delhi"
}

# Why is JSON so popular?
# 1. Human readable
# 2. Programming Language Independent (Python, Java, JavaScript, C#, Go -> supports JSON)
# 3. Lightweight
# 4. API Standard (Application Programmable Interface)


# student_info = {
#     "name": "Tanishq",
#     "age" : 25,
#     25: "Hey",
#     (1, 2): "Hey"
# }

# # Serialization - Converting a python object to JSON [Packing data] 
# student =  {
#     "name": "Moksh",
#     "marks": 99
# }

# # Deserialization - Converting a JSON to a python object [Unpacking data]



# # Part 3 -> Working with JSON in Python
# # function 1 -> dump -> dump data into file (convert python object to JSON)
# student_info =  {
#     "name": "Moksh",
#     "marks": 99
# }

# # with open("student.json", "w") as file:
# #     json.dump(student_info, file)

# # function 2 -> load() [Unpacking] (Conovert JSON to Python Object - Dictionary)
# with open("student.json", "r") as file:
#     data = json.load(file)

# print(data)

# # function 3 -> dumps() -> Convert Python Object to JSON string
# json_string = json.dumps(student_info)
# print(f'JSON string is : {type(json_string)}')

# # function 4 -> loads() -> Convert JSON string into a Python Object [Dict]
# json_string = '{"name": "Abhay Kumar", "marks": 110}'
# print(type(json_string))
# data = json.loads(json_string)
# print(type(data))
# print(data)


# Part 4 -> Handling Nested JSON
with open("student.json", "r") as file:
    data = json.load(file)

# Fetch the state of the student
# print(f'{data['name']} lives in city : {data["address"]["city"]}')

print(f'Salary of {data["employees"][1]["name"]} is {data["employees"][1]["salary"]}')

with open("cleartrip_data.json", "r") as cleartrip_file:
    cleartrip_data = json.load(cleartrip_file)

print(cleartrip_data["filterData"]["onwardLeg"]["nearbyAirportFilter"][0]["airportCode"])