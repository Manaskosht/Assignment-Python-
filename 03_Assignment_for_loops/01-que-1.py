#Write a Python program to print all odd and even numbers from 1 to 20

print("Even numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print( i,end=" ")

print("\nOdd numbers:")
for i in range(1, 21):
    if i % 2 != 0:
        print(i,end=" ")
