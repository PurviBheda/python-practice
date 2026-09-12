"""Simple Calculator

Ask the user for:

first number
second number
operation

Supported operations:

+ 
-
*
/
%

Perform the selected operation.

Handle division by zero properly."""

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter your operation: ")

if operation == "+":
    print("Addition: ", first_number + second_number )
elif operation == "-":
    print("Subtraction: ", first_number - second_number)
elif operation == "*":
    print("Multiplication: ", first_number * second_number)
elif operation == "/":
    print("Division: ", first_number / second_number)
elif operation == "%":
    print("Modulus: ", first_number % second_number)
else:
    print("Invalid Operation")