# Ask the user for their age and check whether they are between 18 and 60 inclusive.

age = int(input("Enter your age: "))
if age >= 18 and age <= 60:
    print("Yes it is")
else:
    print("It's not")