#Take a 3 digit number and extract its: Hundreds, Tens and Ones

num = int(input("Enter your 3 digit number: "))


print("Hundreds", num // 100)
print("Tens", (num // 10) % 10)
print("Ones", num % 10)
