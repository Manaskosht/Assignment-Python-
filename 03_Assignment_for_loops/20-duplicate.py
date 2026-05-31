#Write a Python program to find duplicate letters between two strings.Example: In "virat" and "rohit", the duplicate letter is "r"

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Duplicate letter is : ")
for ch in str1:
    if ch in str2:
        print(ch, end=" ")

        