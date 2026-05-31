#Write a Python program to calculate the sum of numbers between a starting and ending point provided by the user. 
start=int(input("Enter starting number : "))
end=int(input("Enter ending number : "))
sum=0
for i in range (start,end+1):
    sum = sum + i
print("sum :",sum)
