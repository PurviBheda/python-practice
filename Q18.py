"""Create a simple password system using while.

Correct password:

"python123"

Keep asking:

Enter password:

until the user enters the correct password.

Then print:

Login successful"""

password = ""

while password != "python123":
    password = input("Enter password: ")
print("Login Succsessful")