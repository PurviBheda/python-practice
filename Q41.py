"""Mixed Practice ⭐⭐⭐

Start with:

numbers = [40, 10, 50, 20, 30]

Do these operations:

Sort the list in ascending order.
Reverse the sorted list.
Create a copy called new_numbers.
Add 100 to new_numbers.
Print both lists.

Expected final output:

[50, 40, 30, 20, 10]
[50, 40, 30, 20, 10, 100]"""

numbers = [40, 10, 50, 20, 30]
numbers.sort()
numbers.sort(reverse=True)
print(numbers)
new_numbers = numbers
new_numbers.append(100)
print(new_numbers)