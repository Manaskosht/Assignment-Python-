#.Remove Duplicate characters from the string given by the user then print the final output.
text = input("Enter a string: ")
final_char = "" 
for char in text:
    if char not in final_char:
        final_char += char
print("String with duplicate characters removed:", final_char)