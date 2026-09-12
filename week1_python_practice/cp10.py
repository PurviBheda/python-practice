"""Ask the user for a number and check whether it is:

greater than 100
equal to 100
less than 100"""

num = int(input("Enter a number: "))

if num > 100:
    print("Number is greater than 100")
elif num == 100:
    print("Number is equal to 100")
else:
    print("Number is less than 100")