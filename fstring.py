"""Take the user's:

name
city
age

and produce one sentence using an f-string."""

name = input("Enter your name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))


print(f"My name is {name}, I am living in {city} and I am {age} years old.")