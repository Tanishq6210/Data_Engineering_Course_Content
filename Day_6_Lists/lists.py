# List
name1 = "John"
name2 = "Manav"
name3 = "Dorya"
name4 = "Sophie"

# Heterogenous
names = ["John", "Manav", "Dorya", "Sophie", "John"]
names_new = []

for name in names:
    if name == "John":
        continue
    names_new.append(name)
print(names_new)

names.append(1)
# names.insert(0, "Ayush")



print(names.pop())
print(names)

x = [1, 2, 3,]
x.append("456")
# x.append("gkldfdninioafhiobsdfndflkbndlkbnlkdfbns")
print(x)


# print(1 + "hii")
# print(names)
x = [1, 2, 3]
x[1] = x #krishan doubt
print(x)



# List of integers (Revenues)-> sum, avg, count_revenue_gr_2000, highest
# [100, 200, 300, 4000, 1, 6000] 

revenues = [1, 2000, 5000, 9000]

count_gr_2000 = 0
highest = 0
for i in range(len(revenues)):
    revenue = revenues[i]

    if revenue > highest:
        highest = revenue

    if revenue > 2000:
        count_gr_2000 += 1

print(count_gr_2000)