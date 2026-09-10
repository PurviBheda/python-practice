"""Q8 ⭐⭐ — Shopping Check

Create:

cart = ["bag", "shoes", "dress", "watch"]
Ask the user for a product.
Check whether the product exists in the cart using a membership operator."""

cart = ["bag", "shoes", "dress", "watch"]
product = input("Enter your product: ")
if product in cart:
    print(product, "exist in cart")
else:
    print(product, "do not exist in cart")
