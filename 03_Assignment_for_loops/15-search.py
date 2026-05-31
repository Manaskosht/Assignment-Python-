#Write a Python program that allows the user to search for a character within a given string.

str=input("Enter string : ")
char=input("Enter search char : ")
for ch in str:
    if ch == char:
        print("Character found")
        break

