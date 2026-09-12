"""Student Result System

Create a program that asks for:

Student name
Marks

Validate the marks first.

Then display the appropriate grade.

Also print:

Student Name: ______
Marks: ______
Grade: ______
Result: Pass/Fail"""

student_name = input("Enter student name: ")
marks = int(input("Enter marks of student: "))

if marks < 0 or marks > 100:
    print("Invalid marks")

#else: then use if you see something like above

elif marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"


pf = "Pass" if grade != "F" else "Fail"

print("---Student Result System---")
print("Student Name: ", student_name)
print("Marks: ", marks)
print("Grade: ", grade)
print("Pass/Fail: ", pf)