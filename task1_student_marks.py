# Task 1: Create a Dictionary of Student Marks

student_marks = {
    "Rahul": 85,
    "Anita": 92,
    "Suresh": 78,
    "Neha": 88
}

name = input("Enter student name: ")

if name in student_marks:
    print(f"Marks of {name}: {student_marks[name]}")
else:
    print("Student not found.")
