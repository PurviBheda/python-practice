"""Problem 3 — Shopping Check

Create:
cart = ["bag", "shoes", "dress", "watch"]

Ask the user for a product.

Check:
Product available: True/False
Use a membership operator."""


cart = ["bag", "shoes", "dress", "watch"]
enter_product = input("Enter your product: ")
print(enter_product in cart)

