"""Real Practice
python_students = {"A", "B", "C", "D"}
java_students = {"C", "D", "E", "F"}

Find:

Students learning either Python or Java
Students learning both
Students learning only Python
Students learning only Java"""


python_students = {"A", "B", "C", "D"}
java_students = {"C", "D", "E", "F"}

all_students = python_students & java_students
print(all_students)

all_students = python_students | java_students
print(all_students)

all_students = python_students - java_students
print(all_students)

all_students = java_students - python_students
print(all_students)