# Topics for the day
# Designing Systems using OOP
# Combining Classes + Functions + Exceptions
# Writing Maintainable Code
# Introduction to Decorators
# Refactor Script to OOP
# Add Exception Handling
# Create Logging Decorator

# Student Management System
# Student class -> To store individual student details
# Student Manager class -> To store all the students list at one place
# Add a student
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        
        result = func(*args, **kwargs)

        print(f"Finished {func.__name__}")

        return result
    return wrapper

class Student:

    def __init__(self, name, roll_no, marks):
        if not name:
            raise ValueError("Name cannot be empty!")
        
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"
        
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll no: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")

class StudentManager:
    def __init__(self):
        self.students = []

    @logger
    def add_student(self, student):
        # Validation to prevent duplicates
        for existing_student in self.students:
            if existing_student.roll_no == student.roll_no:
                print(f'Roll number : {student.roll_no} already exists!')
                raise ValueError(f'Roll number already exists!')
            

        self.students.append(student)

        print(f"{student.name} added successfully!")

    @logger
    def remove_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)

                print(f"Student removed with roll_no: {roll_no}")
                
                return
        
        print(f"Student with roll no : {roll_no} not found!")

    def search_student(self, roll_no):
        for student in self.students:
            
            if student.roll_no == roll_no:
                return student
            
        return None

    def display_students(self):
        print("Displaying all students below -> ")
        for student in self.students:
            student.display_details()
            print("-"*10)


gdg_manager = StudentManager()
print(gdg_manager.students)

std1 = Student("Vibhore", 21, 99)
std2 = Student("Shachi", 1, 100)
std3 = Student("Ayush", 1, 50)
std4 = Student("Moksh", 4, 10)

gdg_manager.add_student(std1)
# gdg_manager.add_student(std2)
# gdg_manager.add_student(std3)
# gdg_manager.add_student(std4)

# gdg_manager.display_students()

gdg_manager.remove_student(2)

# gdg_manager.display_students()

student = gdg_manager.search_student(2)
# if student == None:
    # print("Student not found!")
# else:
    # student.display_details()

# gdg_manager.display_students()



# Decorators
# Decorator structure
def decorator_function(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper

@decorator_function
def greet():
    print("Hello!")

# greet = decorator_function(greet)

greet()