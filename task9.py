#Take a number and calculate its quotient and remainder when divided by another number

num = int(input("Enter a number: "))
divisor = int(input("Enter another number: "))

quotient = num // divisor
remainder = num % divisor

print("Quotient:", quotient)
print("Remainder:", remainder)