"""Ask the user for marks and check whether they passed.

Passing marks = 40."""

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else: 
    print("Fail")