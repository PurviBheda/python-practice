"""Problem 1 — Eligibility Checker
Take:
Age
from the user.
Check whether the person is between 18 and 60, inclusive.
Your output should be a Boolean:

Eligible: True
Use comparison + logical operators."""

age = int(input("Enter your Age: "))
print(age >= 18 and age <= 60)

