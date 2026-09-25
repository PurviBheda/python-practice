"""append() and insert() ⭐⭐

Given:

subjects = ["Python", "SQL", "Java"]

Do the following:

Add "HTML" at the end.
Insert "CSS" between "Python" and "SQL".

Print the final list.

Expected:

["Python", "CSS", "SQL", "Java", "HTML"]"""

subjects = ["Python", "SQL", "Java"]
subjects.append("HTML")
subjects.insert(1, "CSS")
print(subjects)
