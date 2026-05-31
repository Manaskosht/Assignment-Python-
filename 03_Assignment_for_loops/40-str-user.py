#Count how many digits in a string entered by the user. 
#text=”sytax_error2806 hai ” 

text = input("Enter a string: ")
digit_count = 0
for char in text:
    if char.isdigit():
        digit_count += 1
print("Number of digits in the string:", digit_count)
