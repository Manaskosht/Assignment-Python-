#Write a Python program to display all possible pairs of 3.

for i in range(1, 4):
    for j in range(1, 4):
        if i==3 or j==3:
          print(i, ":", j)