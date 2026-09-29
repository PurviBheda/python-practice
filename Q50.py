"""Q1 — Create

Create a dictionary called student containing:

name → your name
age → your age
course → MCA
city → your city

and

Print only the:

name
course

using dictionary keys."""

student = {
    "name" : "Purvi Bheda",
    "age" : 21,
    "course" : "MCA",
    "city" : "Surat"
}

"""print(student["name"])
print(student["course"])"""

#print(student.get("city"))
#print(student.get("phone"))



"""Update

Change the student's age and add:

"skills" → "Python"

using update()."""

"""student.update({"age" : 22})
print(student)"""

#student.update({"skills" : "Python"})


del student["city"]
print(student)