"""Problem 5 ⭐⭐ — Login Check

Create:

username = "purvi"
password = "python123"

Ask the user for username and password.

Use nested conditions:

Correct username + correct password → Login successful
Correct username + wrong password → Wrong password
Wrong username → Wrong username""""""
"""


username = "purvi"
password = "python123"

e_u = input("Enter Username: ")
e_p = input("Enter Password: ")

if e_u == username:
    if e_p == password:
        print("Login Successful!")
    else:
        print("Incorrect Passowrd")
else:
    print("Incorrect Username")

