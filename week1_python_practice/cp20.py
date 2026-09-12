"""Create a shopping discount calculator.

Ask for the total purchase amount:

₹5000 or more → 20% discount
₹3000–₹4999 → 15%
₹1000–₹2999 → 10%
below ₹1000 → no discount

Print:

original amount
discount
final amount"""

amount = int(input("Enter your total purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000 and amount <= 4999:
    discount = amount * 0.15
elif amount >= 1000 and amount <= 2999:
    discount = amount * 0.10
else:
    print("No Discount")

print("-----Shopping Discount Calculator-----")
print("Original amount", amount)
print("Discount", discount)
print("Final Amount", amount - discount)