"""Create a simple ATM eligibility checker.

Ask for:

age
account balance

The user can withdraw money only if:

age is at least 18
balance is greater than ₹500

Print an appropriate message."""

age = int(input("Enter your age: "))
a_b = int(input("Enter your account balance: "))

if age >= 18:
    if a_b > 500:
        print("You can withdraw your money")
    else:
        print("You do not have enough money")
else:
    print("You are not eligible")