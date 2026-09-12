"""16. Create a program that accepts marks from 0 to 100 and prints:

90–100 → A+
75–89 → A
60–74 → B
40–59 → C
Below 40 → Fail

Also reject marks below 0 or above 100."""


marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Reject")
elif 90 <= marks <= 100:
    print("A+")
elif 75 <= marks <= 89:
    print("A")
elif 60 <= marks <= 74:
    print("B")
elif 40 <= marks <= 59:
    print("C")
else:
    print("Fail")
