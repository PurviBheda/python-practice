"""Sentence Analyzer
Take a sentence from the user.

Display:

Uppercase:
Lowercase:
Number of words:
Number of 'a':

You'll need:

upper()
lower()
split()
count"""

print("---Sentence Analyzer---")
sentence = input("Enter any sentence: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.split())
print(sentence.count("p"))

