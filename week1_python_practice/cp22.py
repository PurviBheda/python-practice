"""Login + Role System

Ask for:

username
password
role

Valid credentials:

username = "purvi"
password = "python123"

Roles:

admin
student

If credentials are incorrect → "Invalid Login"

If correct:

admin → "Welcome Admin"
student → "Welcome Student"

Anything else → "Invalid Role" """

username = "purvi"
password = "python123"


entered_username = input("Enter Username: ")
entered_password = input("Enter Password: ")
entered_role = input("Enter Role: ")

if entered_username == username:
    if entered_password == password:
        if entered_role == "admin":
            print("Welcome Admin")
        elif entered_role == "student":
            print("Welcome Student")
        else:
            print("Invalid Role")
    else:
        print("Incorrect Password")
else:
    print("Invalid Login")
    