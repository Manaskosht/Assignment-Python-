#Given : 01275623
#Write a Python program to find and print the greatest character in the string.


text = "01275623"
grt = text[0]
for ch in text:
    if ch > grt:
        grt = ch
print("Greatest character is:", grt)