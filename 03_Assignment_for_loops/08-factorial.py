#Write a Python program to calculate the factorial of a number provided by the user

num=int(input("Enter number :"))
fac=1
for i in range(1,num+1):
    fac=i*fac
print("fact of",i ,"=" ,fac)
    