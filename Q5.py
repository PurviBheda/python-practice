"""Q5 ⭐⭐ — Voting Eligibility

Take age from the user.

If age is 18 or above:
Eligible to vote
Otherwise:
Not eligible to vote"""

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")