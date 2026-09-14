"""Take a number from the user and print its multiplication table from 1 to 10.

Example:

Enter number: 5

5
10
15
20
...
50"""

num = int(input("Enter a number: "))

for i in range(1,11):
   print(num * i)