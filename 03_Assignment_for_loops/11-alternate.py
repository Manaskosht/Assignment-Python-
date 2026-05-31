#Write a Python program to print alternate characters from a given string.

str = input("Enter chr : ")
for i in range(0, len(str), 2):
    print(str[i], end="")
