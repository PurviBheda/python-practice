"""Text Cleaner

Take a sentence that may contain extra spaces and different capitalization.

Clean it by:

removing beginning/end spaces
converting it to lowercase
replacing "java" with "python"

Example:

Enter sentence:   I LOVE JAVA   🎯

Output:

i love python 🎯"""

sentence = input("Enter any sentence: ")
sentence = sentence.strip().lower().replace("java", "python")
print(sentence)