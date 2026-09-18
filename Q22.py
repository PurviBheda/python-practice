"""Email Checker

Take an email from the user.

Check whether it ends with:

@gmail.com

Use endswith()."""

mail = input("Enter your email id: ")
print(mail.endswith(".com"))

