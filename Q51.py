"""Keys, Values, Items

Given:

student = {
    "name": "Purvi",
    "age": 20,
    "course": "MCA",
    "city": "Surat"
}

Print:

All keys
All values
All key-value pairs"""

student = {
    "name": "Purvi",
    "age": 20,
    "course": "MCA",
    "city": "Surat"
}
"""print(student.keys())
print(student.values())
print(student.items())"""

for key,value in student.items():
    print(key, ":", value)