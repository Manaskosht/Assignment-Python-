#Write a Python program to reverse a string entered by the user.

str=input("Enter char :")

rev=""
for i in str:
    rev=i+rev
print(rev) 
