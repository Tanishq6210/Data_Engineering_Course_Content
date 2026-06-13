# Enter a string:
#    hello world python

# ===== STRING MENU =====
# 1. Strip Spaces
# 2. Find a Substring
# 3. Capitalize String
# 4. Convert to Uppercase
# 5. Convert to Lowercase
# 6. Convert to Title Case
# 7. Replace a Word
# 8. Count Occurrences
# 9. Check Starts With
# 10. Check Ends With
# 11. Split String
# 12. Exit

# Enter your choice: 3

# Result:
# Hello world python


# Note: The menu should contain atleast 10 new functions which were not covered in the class


# Ques 5
def demo(*args):
    print(len(args))

demo(10, 20, 30)


# Ques 7
square = lambda x: x * x
print(square(4))


# Ques 10
numbers = [1, 2, 3]

result = list(
    map(lambda x: x*2, numbers)
)

print(result)

# Ques 12
numbers = [1,2,3,4,5]

result = list(
    filter(lambda x:x>3, numbers)
)

print(result)

# Ques 13
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(10, 20, name="Rahul")
# option A
(10, 20)
{'name': 'Rahul'}

# option B
[10,20]
['Rahul']

# option C
# 10 20 Rahul

# option D

# Ques 14
marks = [50, 60, 70]

result = list(
    map(lambda x:x+5, marks)
)

print(result)


# Ques 15
numbers = [10, 15, 20, 25, 30]

result = list(
    filter(lambda x:x%10==0, numbers)
)

print(result)
# Ques 16
# def fun(**kwargs, *args):
#     print(kwargs)
#     print(args)

# fun(name = "Shachi", 1, 2)


# option A
# Shachi
# (1,2)

# Option B
# (1, 2)
# Shachi

# Option C
# (1)
# Shachi
# (2)