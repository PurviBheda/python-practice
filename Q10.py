"""Q10 ⭐⭐⭐ — Student Result System

Take:

Student name
Marks

First check whether the marks are valid:

0 to 100
If invalid:
Invalid marks

Otherwise calculate the grade:

90–100 → A+
75–89 → A
60–74 → B
40–59 → C
Below 40 → Fail

Use if, elif, else."""


student_name = input("Enter student name: ")
marks = int(input("Enter student marks: "))

print("---Student Result System---")
print("Student Name: ", student_name)
print("Marks: ", marks)

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90 and marks <= 100:
    print("A+")
elif marks >= 75 and marks <= 89:
    print("A")
elif marks >= 60 and marks <= 74:
    print("B")
elif marks >= 40 and marks <= 59:
    print("C")
else:
    print("Fail")