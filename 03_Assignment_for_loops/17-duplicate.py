#Write a Python program to filter out duplicate characters from a string entered by the user.

str=input("Enter a string: ")
res=""
for ch in str:
    if ch not in res:
        res = res + ch
print("String filter out duplicates:", res)

