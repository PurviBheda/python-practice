"""Real Practice ⭐

Create:

products = {
    "Laptop": 55000,
    "Phone": 25000,
    "Tablet": 18000,
    "Watch": 5000
}

Then:

Print the price of the Laptop.
Add "Camera": 30000.
Change Phone price to 28000.
Delete Watch.
Print every product and price using a loop."""

products = {
    "Laptop": 55000,
    "Phone": 25000,
    "Tablet": 18000,
    "Watch": 5000
}

print(products.get("Laptop"))

products.update({"Camera" : 30000})
print(products)

products.update({"Phone" : 28000})
print(products)

del products["Watch"]
print(products)

for key,value in products.items():
    print(key, ":", value)