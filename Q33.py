"""Mixed Practice ⭐⭐⭐

Start with:

shopping = ["Milk", "Bread", "Eggs"]

Do these operations in order:

Add "Butter" at the end.
Insert "Rice" at index 1.
Change "Eggs" to "Cheese".
Remove "Milk" using remove().
Remove the last item using pop().
Print the final list."""

shopping = ["Milk", "Bread", "Eggs"]
shopping.append("Butter")
shopping.insert(1, "Rice")
shopping[2] = "Cheese"
shopping.remove("Milk")
shopping.pop()
print(shopping)