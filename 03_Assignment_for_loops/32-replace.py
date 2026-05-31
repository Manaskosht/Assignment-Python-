#.Task: Replace Character in String 
#Write a program that takes a string input from the user, then asks for a character 
#to replace and the character to replace it with. The program should output the 
#modified string where all occurrences of the specified character are replaced by the replacement character.

text = input("Enter a string: ")
replace = input("Enter the character to replace: ")
char_with = input("Enter the character to replace with: ")
modified_text = text.replace(replace, char_with)
print("Modified string:", modified_text)