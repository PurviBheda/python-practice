"""Unpacking ⭐⭐

Given:

person = ("Purvi", 20, "Surat")

Unpack it into:

name
age
city

Then print each variable"""

"""person = ("Purvi", 20, "Surat")
name, age, city = person
print(name)
print(age)
print(city)"""








"""Single-item Tuple ⭐⭐

Create a tuple containing only the number 100.

Then use type() to verify that it is a tuple."""

"""number = (100,)
print(type(number))"""




"""Immutability ⭐⭐

Create:

numbers = (10, 20, 30)

Try to change 20 into 25.

Observe the error."""

numbers = (10, 20, 30)
numbers[1] = 40
print(numbers)