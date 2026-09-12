"""lectricity Bill Calculator

Ask the user for electricity units.

Calculate the bill:

0–100 units → ₹5/unit
101–200 → ₹7/unit
Above 200 → ₹10/unit

Also print the total bill."""

e_units = int(input("Enter your electricity units: "))

if e_units >= 0 and e_units <= 100:
    unit = e_units * 5.00
elif e_units >= 101 and e_units <= 200:
    unit = e_units * 7.00
else:
    unit = e_units * 10.00

print("Total Bill: ", unit)