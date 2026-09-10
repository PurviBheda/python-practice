"""Q7 ⭐⭐ — Login System

Create:

username = "purvi"
password = "python123"
Ask the user for username and password.
Use nested conditions."""

username = "purvi"
password = "python123"

entered_username = input("Enter Username: ")
entered_password = input("Enter Password: ")

print("---Login system---")
if entered_username == username:
    if entered_password == password:
        print("Login Successful")
    else:
        print("Incorrect Passowrd")
else:
    print("Incorrect Username")