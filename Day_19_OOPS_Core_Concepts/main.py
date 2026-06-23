# Part 0 : Recap & Quizz
# Part 1 : Introduction to Inheritance
# Part 2 : Parent Class & Child Class
# Part 3 : Method Overriding
# Part 4 : Encapsulation
# Part 5 : Getter & Setter Methods
# Part 6 : FileProcessor Project
# Part 7 : CSVProcessor & JSONProcessor
# Part 8 : Private Variables & Access Control

# Inheritance -> It is a concept where one class acquired the properties and behaviour of another class


# Parent class, super class, base class -> Parent class
# Inherited class, child class
import os
# Parent class
class Animal:
    def sound(self):
        print("Animal making sound!")

# Child class
class Dog(Animal):
    
    def sound(self):
        self.sound()
        print("Bark!!")

class LabraDog(Dog):
    def sound(self):
        self.sound()
        print("Labra Barks!")
    pass

class Cat(Animal):
    # def sound(self):
    #     print("Meoww!")
    pass

animal = Animal()
animal.sound()

dog1 = Dog()
dog1.sound()

cat = Cat()
cat.sound()

labra_dog = LabraDog()
labra_dog.sound()

class FileProcessor:

    def validate_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} not found!")

    def log(self, message):
        print(f"[LOG] {message}")

    def read(self):
        raise NotImplementedError("Child class must implement read()")

class CsvProcessor(FileProcessor):
    def read(self):
        print("Reading a CSV file!")
        

class JsonProcessor(FileProcessor):
    
    def read(self):
        self.validate_file()
        print("Reading a Json file!")
        pass

class TextFileProcessor(FileProcessor):
    pass

# Method overriding - It occurs when a child class provides its own implementation of a method already defined in the parent class

csv_processor = CsvProcessor()
csv_processor.read()

json_processor = JsonProcessor()
json_processor.read()

txt_file_processor = TextFileProcessor()
txt_file_processor.read()

# You have an ATM machine
# withdraw, deposit, check balance

# Encapsulation -> It means hiding internal implementation details and controlling how data is processed

# Goal of encapsulation -> To protect data from accidentail modification

# Why encapsulation
balance = 100000

balance = -1000

class InvalidAmountException(Exception):
    pass

class InvalidUserError(Exception):
    pass
class BankAccount:

    def __init__(self, name, account_balance):
        # public variable / attribute -> They can be accessed from anywhere
        self.name = name
        # Private variable / attribute -> They can only be accessed within the class they are defined in
        self.__account_balance = account_balance

    # Setter Method
    def set_account_balance(self, account_balance):
        # Authentication
        if account_balance < 0:
            raise InvalidAmountException("Amount is less than 0!")
        self.__account_balance = account_balance

    # Getter Method
    def get_account_balance(self):
        # username and password
        if self.name != "Mohit Pandey":
            raise InvalidUserError(f"{self.name} is not the account owner!")
        return self.__account_balance




mohit_account = BankAccount("Mohit Pandey", 100000)
# print(mohit_account.account_balance)
mohit_account.name = "Rohit"
# Any random person
print(mohit_account.name)
print(mohit_account.get_account_balance())
mohit_account.set_account_balance(1000)
print(mohit_account.get_account_balance())
# print(mohit_account.account_balance)

list1 = [1, 3, 2]
list2 = [3, 1, 2]

print(list1.sort())
print(list2.sort())

class A:
    def __init__(self, name):
        self._name = name


# super() -> This function is used to call the parent class properties or methods from the chil class
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no #public attribute -> Visible everywhere
        self._name = name #protected attribute -> Parent and derived classes
        self.__address = "Gurugram" #private attribute -> Only in the class where it is defined

    
    def displayStudent(self):
        print("Displaying Student!")

class BtechStudent(Student):
    def __init__(self, roll_no, name):
        super().__init__(roll_no, name)


    def display_student(self):
        super().displayStudent()
        print("Displaying Btech Student!")

    def display_student_name(self):
        print(f"Name: {self._name}")
    
    def display_student_address(self):
        print(f"Address: {self.__address}")


std1 = BtechStudent(20, "Arul Bansal")
std1.display_student_name()
std1.display_student_address()

# print(std1._name)