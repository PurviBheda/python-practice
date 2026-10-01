"""Nested Dictionary

Create:

student = {
    "name": "Purvi",
    "address": {
        "city": "Surat",
        "state": "Gujarat"
    }
}

Print:

Name
City
State"""

"""student = {
    "name": "Purvi",
    "address": {
        "city": "Surat",
        "state": "Gujarat"
    }
}

print(student["name"])
print(student["address"]["city"])
print(student["address"]["state"])

student["address"]["city"] = "Mumbai"
print(student["address"]["city"])
"""





"""List of Dictionaries

Create:

students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 75},
    {"name": "C", "marks": 90}
]

Print the marks of student "B"."""

students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 75},
    {"name": "C", "marks": 90}
]
#print(students[1]["marks"])

for mark in students:
    print(mark["marks"])