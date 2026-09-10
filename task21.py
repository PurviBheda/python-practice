"""Problem 6 ⭐⭐⭐ — Conditional Expression

Take a number and use a conditional expression to store:

"Even" or "Odd" in a variable.

Example idea:
result = ______
print(result)
"""

num = int(input("Enter a number: "))
result = "Even" if num%2==0 else "Odd"
print(result)