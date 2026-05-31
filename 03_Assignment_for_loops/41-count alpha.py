#Count only alphabets (both uppercase and lowercase). 
#Enter a string:  this123 i am  
#Number of letters: 7

text = input("Enter a string: ")
letter_count = 0
for char in text:
    if char.isalpha():
        letter_count += 1
print("Number of letters:", letter_count)
