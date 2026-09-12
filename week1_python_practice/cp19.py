"""Create a password strength checker.

Ask the user for a password.

Check:

password length is at least 8 characters
password is not "password"

Print "Strong enough" or "Weak password"."""

p_w = input("Enter your password: ")

if p_w == "password":
    print("You can not add password as password")
elif len(p_w) >= 8:
    print("Strong enough")
else:
    print("Weak password")