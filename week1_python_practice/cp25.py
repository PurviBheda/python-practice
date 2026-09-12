"""Mini Eligibility System 🧠

Ask the user for:

age
marks
income

A student is eligible for a scholarship only if:

age is between 18 and 25
marks are at least 75
income is below ₹3,00,000

Print whether the student is eligible or not."""


age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
income = int(input("Enter your income: "))

if age >= 18 and age <= 25:
    if marks >= 75:
        if income < 300000:
            print("You are eligible for scholarship")
        else:
            print("Income criteria is bigger")
    else:
        print("Your marks is below 75 so that you're not eligible for scholarship")
else:
    print("You are not eligible")