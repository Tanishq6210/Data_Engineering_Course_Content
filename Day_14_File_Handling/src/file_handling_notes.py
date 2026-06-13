import csv

# Data storing formats -> .txt, .xlsx, .csv
# ETL
# 1. Extract -> Extraction of the data from the data source (file)
# 2. Transform -> Transform / Clean the original data to get a usable, commulative data
# 3. Load -> Loading of the transformed data into the destination (file)

# Syntax to open a file -> open(), A built-in function
# file = open("filename.txt", "mode")

# r -> reading mode, w -> writing, a -> appending, r+ -> reading + writing
# file = open("../data/data.txt", "r")
# print(file.read()) # To read the entire content of the file

# Why is closing important? -> 1. Release memory, 2. Prevents corruption, 3. Good programming practice, 4. Other application can access the resource
# file.close() #Manually closed the resource


# Context Manager

# Reading Text Files
# 1. .read() -> It returns the entire content in a single string format
# 2. .readlines() -> It return the entire content, splitted into multiple lines in the form of a list

content = ""

# Extraction
with open("../data/input/data.txt", "r") as file: #It will automatically call, .close() function
    content = file.readline()
    print(content)
    content = file.readline()
    print(content)



# no_of_words = len(content.split(" "))


# # Loading
# # Writing text files
# with open("../data/result_file.txt", "a") as file:
#     file.writelines(f'No. of words: {no_of_words}')


# CSV -> Comma Seperated Values
# Advantages of a CSV
# 1. Easy to store data
# 2. Human Readable
# 3. Excel Compatible


filtered_students = [["marks", "name", "id"]]
# Open a csv file
with open("../data/input/students.csv", "r") as in_file, open("../data/output/csv_output.csv", "w", newline="") as out_file:
    reader = csv.reader(in_file)
    next(reader) #It skips the first row (header).

    for row in reader:
        if int(row[2]) > 50:
            filtered_students.append(row)


    # print(filtered_students)

    writer = csv.writer(out_file)

    writer.writerows(filtered_students) # Write all the rows at once


with open("../data/input/students.csv", "r") as file, open("../data/output/filtered_students.csv", "w", newline = "") as filtered_file:
    fieldnames = ["name", "marks", "roll_no"]
    reader = csv.DictReader(file)
    writer = csv.DictWriter(filtered_file, fieldnames = fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        if int(row["marks"]) > 50:
            writer.writerow(row)
