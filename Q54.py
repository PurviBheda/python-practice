"""Conditional

Given:

marks = {
    "A": 85,
    "B": 45,
    "C": 72,
    "D": 30,
    "E": 90
}

Create a new dictionary containing only students who scored 60 or above.

Expected:

{
    "A": 85,
    "C": 72,
    "E": 90
}"""

marks = {
    "A": 85,
    "B": 45,
    "C": 72,
    "D": 30,
    "E": 90
}

passed = {
    name :  mark
    for name,mark in marks.items()
    if mark >= 60
}
print(passed)