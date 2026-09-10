"""Problem 3 ⭐⭐ — Marks Grade

Take marks from the user.

Use:

90+ → A+
75–89 → A
60–74 → B
40–59 → C
Below 40 → Fail

Use if, elif, and else."""

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A+")
elif marks >= 75 and marks <= 89:
    print("A")
elif marks >= 60 and marks <= 74:
    print("B")
elif marks >= 40 and marks <= 59:
    print("C")
else:
    print("Fail")