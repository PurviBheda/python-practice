"""Real Practice ⭐

Given:

products = {
    "Laptop": 55000,
    "Phone": 25000,
    "Tablet": 18000,
    "Watch": 5000,
    "Camera": 30000
}

Create a new dictionary containing only products costing ₹20,000 or more.

Expected:

{
    "Laptop": 55000,
    "Phone": 25000,
    "Camera": 30000
}"""

products = {
    "Laptop": 55000,
    "Phone": 25000,
    "Tablet": 18000,
    "Watch": 5000,
    "Camera": 30000
}

expensive = {
    goods : price
    for goods,price in products.items()
    if price >= 20000
}

print(expensive)