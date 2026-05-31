#Write a Python program to generate a table of a number provided by the user.

num=int(input("Enter your number : "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")