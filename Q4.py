"""Q4 ⭐ — Number Comparison

Take two numbers.

Print:

First number is greater
Second number is greater
Both are equal

Use if, elif, and else."""

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

if first_number > second_number:
    print("First number is greater")
elif first_number < second_number:
    print("Second number is greater")
else:
    print("Both are equal")

