#Write a Python program to calculate the product of numbers between a starting and ending point provided by the user.

start=int(input("Enter starting number : "))
end=int(input("Enter ending number : "))
product=1
for i in range (start,end+1):
    product = product * i
print("Product :",product)
