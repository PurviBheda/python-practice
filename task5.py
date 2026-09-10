#Take marks of 5 subjects and calculate total percentage

c = int(input("Enter marks of C Language: "))
py = int(input("Enter marks of Python Langauge: "))
j = int(input("Enter marks of Java Langauge: "))
db = int(input("Enter marks of DBMS: "))
iot = int(input("Enter marks of IOT: "))

total_marks = c + py + j + db + iot
print("Percentage: ", total_marks / 5)