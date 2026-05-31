# Print all characters from the string that are at odd indices. 

text = "Hello, World!"
for i in range(len(text)):
    if i % 2 != 0:
        print(text[i])
        