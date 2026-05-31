#Write a Python program to check if a number provided by the user is prime or not

num=int(input("Enter your number :"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count == 2:
    print("This is Prime Number")
else:
    print("This is not a Prime Number")
