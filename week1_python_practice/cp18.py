"""Create a number comparison program.

Take two numbers and print:

First number is greater
Second number is greater
Both are equal"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is greater")
elif num1 < num2:
    print("Second number is greater")
else:
    print("Both are equal")