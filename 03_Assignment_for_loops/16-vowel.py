#Write a Python program to filter out all vowels and consonants from a string entered by the user

str = input("Enter a string: ")
vow = ""
cons = ""
for ch in str:
    if ch in "aeiouAEIOU":
        vow=vow + ch
    else:
        cons=cons + ch
print("Vowels:", vow)
print("Consonants:", cons)