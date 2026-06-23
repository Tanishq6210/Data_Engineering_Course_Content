list1 = [1, 3, 2]
list2 = [4, 1, 2]

print(list1.sort())
print(list2.sort())

print(list1)
print(list2)

if list1.sort() == list2.sort():
    print("Same")
else:
    print("Not same")

# age, gae, aeg, def, fed, fde

# aeg -> age, gae, aeg
# def -> def, fed, fde