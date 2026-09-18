"""Simple Username Checker

Take a username from the user.

Clean any extra spaces and convert it to lowercase.

Then check whether it starts with:

admin

For example:

Enter username:   AdminPurvi

Result:

True

Hint: you'll need two methods together."""

"""print("---Simple Username Checker---")
username = input("Enter your Username: ")
username = username.strip().lower()
print(username.startswith("Admin"))
"""

print("---Simple Username Checker---")

username = input("Enter your Username: ")

username = username.strip().lower()

print(username.startswith("admin"))
