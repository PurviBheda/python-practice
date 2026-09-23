"""Mixed Challenge ⭐⭐⭐

Given:

student = ("Purvi", 20, "BCA", 8.3)

Do all of these:

Print "Purvi" using indexing.
Print 8.3 using indexing.
Unpack the tuple into name, age, course, and cgpa.
Print all four variables.
Try changing "BCA" to "MCA".
Explain in one sentence why the change doesn't work."""

student = ("Purvi", 20, "BCA", 8.3)
print(student[0])

print(student[3])

name, age, course, cgpa = student
print(name)
print(age)
print(course)
print(cgpa)

student[2] = "MCA"


