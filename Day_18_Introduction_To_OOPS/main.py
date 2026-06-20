student_name_1 = "Moksh"
student_age_1 = 20
student_roll_no_1 = 190


student_name_2 = "Hitesh"
student_age_2 = 21
student_roll_no_2 = 191

student_name_3 = "Hitesh"
student_age_3 = 21
student_roll_no_3 = 191

student_list = [
    {
        "student_name_1" :"Moksh",
        "student_age_fiu_1": 20,
        "std_roll_no_1":190,
        "attendance": 80,
        "std_address": "Delhi"
    },
    {
        "student_name_2" :"Moksh",
        "student_age_2": 20,
        "student_roll_no_2":190,
        "attendance": 80
    },
    {
        "student_name_3" :"Moksh",
        "student_age_3": 20,
        "student_roll_no_3":190,
        "attendance": 80
    }
]

# def isValidAttendance(name = "Moksh"):
    # iterate list
    # find at which index moksh is present
    # check attendance


# Advantage of OOP
# 1. Code Organisation
# 2. Reusability
# 3. Real-World Problem

# Defining a class
class Student:
    
    # Constructor - It is a function that runs automatically once the object is created
    def __init__(self, name, roll_no, age, attendance):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.attendance = attendance

    # self = student_shachi 
    def is_attendance_valid(self):
        if self.attendance >= 75:
            return True
        else:
            return False
        
    def display_student_info(self):
        print(f"Stuent Details:")
        print(f"Student name: {self.name}")
        print(f"Student age: {self.age}")
        print(f"Student roll_no: {self.roll_no}")
        print(f"Student attendance: {self.attendance}")
    
# s_1 == self
# Student.__init__(s_1, "Moksh", 190, 21)
# Defining & Instantiating object
s_1 = Student("Moksh", 190, 21, 90)
print(f"Name of the student is {s_1.name}, age: {s_1.age}, roll_no: {s_1.roll_no}")

# Student.__init__(student_hitesh, "Moksh", 190, 21)
s_2 = Student("Hitesh", 191, 20, 91)
print(f"Name of the student is {s_2.name}, age: {s_2.age}, roll_no: {s_2.roll_no}")

s_3 = Student("Shachi", 192, 22, 65)
print(f"Name of the student is {s_3.name}, age: {s_3.age}, roll_no: {s_3.roll_no}")


print(f"Is attendance valid for {s_2.name}? {s_2.is_attendance_valid()}")

print(f"Is attendance valid for {s_3.name}? {s_3.is_attendance_valid()}")

# s_1.display_student_info()

s_1.name = "Tanishq"
s_2.age = 100
s_3.attendance = 99

s_1.display_student_info()
s_2.display_student_info()
s_3.display_student_info()


class ExtractCSV:

    def __init__(self, filepath):
        self.filepath = filepath

    def extract_csv(self):
        with open(self.filename, "r") as file:
            return file.read()


csv_1 = ExtractCSV("abc.csv")
csv_2 = ExtractCSV("xyz.csv")

# class CsvOperation:

# class ExtractJSON:
