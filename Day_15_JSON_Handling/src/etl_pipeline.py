import csv
import json


employees = []
total_salary = 0

with open("employee.csv", "r") as employee_file:
    reader = csv.DictReader(employee_file)

    for row in reader:
        # Replace missing salary with 0
        if row["salary"] == "":
            row["salary"] = 0
        else:
            row["salary"] = int(row["salary"])

        total_salary = total_salary + row["salary"]
        employees.append(row)

average_salary = total_salary / len(employees)


employees_json_output = {
    "employees": employees,
    "average_salary": average_salary
}


# Write dictionary (python object) into a JSON file
with open("employee_output.json", "w") as output_file:
    json.dump(employees_json_output, output_file, indent = 4)

print("Data exported successfully!")