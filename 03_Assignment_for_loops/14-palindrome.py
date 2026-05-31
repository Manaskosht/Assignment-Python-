#Write a Python program to check whether a string entered by the user is a palindrome.

char=input("Enter str: ")
rev=""
for i in char:
    rev=i+rev
if char == rev:
    print("String is palindrom")
else:
    print("String is not palindrom")
    
    