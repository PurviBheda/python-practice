"""3. Ask the user for username and password.

Correct username:

purvi

Correct password:

python123

Print "Login Successful" only when both are correct."""


username = "purvi"
password = "python123"

entered_username = input("Enter Username: ")
entered_password = input("Enter Passowrd: ")

if entered_username == username:
    if entered_password == password:
        print("Login Successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect credentials")