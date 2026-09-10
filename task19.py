"""Problem 4 ⭐⭐ — Age Category

Take age from the user.

Print:

Below 13 → Child
13–19 → Teenager
20–59 → Adult
60+ → Senior Citizen"""


age = int(input("Enter your Age: "))
if age <= 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior Citizen")