"""Q6 ⭐⭐ — Grade Calculator

Take marks and display:

90+ → A+
75–89 → A
60–74 → B
40–59 → C
Below 40 → Fail"""


marks = int(input("Enter your marks: "))

print("---Grade Calculator---")
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