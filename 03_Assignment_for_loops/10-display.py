#Write a Python program to display all letters except 'm' and 'i' from the string "Dreamer infotech".

str="Dreamer infotech"
for i in str:
    if i != "m" and i != "i":
        print(i, end="")

