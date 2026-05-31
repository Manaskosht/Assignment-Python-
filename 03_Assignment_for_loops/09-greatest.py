#Write a Python program to find the greatest character from the string "python".

str="python"
grt=str[0]
for ch in str:
    if str>grt:
        grt=ch
print("Greatest character is :",grt)