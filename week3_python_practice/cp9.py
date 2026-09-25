"""Mini Program 🏆
Student Marks Analyzer

Create a Python program that manages student marks.

Start with:

marks = [78, 65, 90, 55, 88, 72, 95]

Your program must do the following:

Step 1

Print the original marks.

Step 2

Add 82 to the list using append().

Step 3

Insert 70 at index 2.

Step 4

Remove 55 using remove().

Step 5

Create a copy called:

sorted_marks

Don't modify the original list when sorting.

Step 6

Sort sorted_marks in ascending order.

Step 7

Create a new list called high_marks using list comprehension containing only marks greater than or equal to 80.

Step 8

Print:

Original marks:
Sorted marks:
High marks:
Highest mark:
Lowest mark:
Expected structure

Your final output should look approximately like:

Original marks: [...]
Sorted marks: [...]
High marks: [...]
Highest mark: ...
Lowest mark: ...

Don't copy the exact solution. Build it yourself."""

print("---Student Marks Analyzer---")
marks = [78, 65, 90, 55, 88, 72, 95]
print(marks)

marks.append(82)

marks.insert(2, 70)

marks.remove(55)

sorted_marks = marks.copy()

sorted_marks.sort()

print("Original Marks: ", marks)
print("Sorted Marks: ", sorted_marks)