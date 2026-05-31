#Take string from user and Replace every vowel in the string with an asterisk
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
modified_text = ""
for char in text:
    if char in vowels:
        modified_text += "*"
    else:
        modified_text += char
print("Modified string:", modified_text)