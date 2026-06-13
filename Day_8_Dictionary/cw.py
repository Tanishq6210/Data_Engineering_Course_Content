
# Make a student information system using a dictionary where the key is the student ID and the value is another dictionary containing the student's name and marks. 

# 1. Add Student: This option should allow the user to add a new student to the system by providing the student ID, name, and marks.
# 2. View All Students: This option should display the details of all students in the system.
# 3. Update Marks: This option should allow the user to update the marks of an existing student
# 4. Search Student: This option should allow the user to search for a student by their ID and display their details.
# # 5. Find Topper: This option should find and display the details of the student with the highest marks.

student = {

}

#Find topper
topper_marks = 0
topper_name = None
for student_id, student_info in student.items():
    print(student_id, student_info)

    total_marks_of_a_student = 0
    for subject_name, subject_marks in student_info["marks"].items():
        total_marks_of_a_student += subject_marks

    if total_marks_of_a_student > topper_marks:
        topper_marks = total_marks_of_a_student
        topper_name = student_info["name"]


print(f'Topper name: {topper_name}, Topper Marks: {topper_marks}')

student[1] = {
    "name": "Tanishq",
    "marks": {
        "maths": 98
    }
}
print(student)



# Create a matrix1
# Create another matrix2, that will contain rows which has even first element
 
mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
] 