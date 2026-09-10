"""Q9 ⭐⭐⭐ — Conditional Expression

Take a number from the user.
Using a conditional expression, store whether the number is:
Even or Odd
Then print the result.
You must use a conditional expression, not a normal if-else."""

num = int(input("Enter your number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(result)