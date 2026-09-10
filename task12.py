"""Problem 2 — Login Check

Create:
username = "purvi"
password = "python123"
Ask the user to enter username and password.
Check whether both are correct."""

username = "purvi"
password = "python123"

entered_username = (input("Enter Username: "))
entered_password = (input("Enter Password: "))

print(entered_username == username and entered_password == password)


