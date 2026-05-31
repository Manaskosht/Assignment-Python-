#Given: text = "knowyourself"
#Goal: Find and print the first character that repeats


text = "knowyourself"
for i in text:
    c = 0
    for j in text:
        if i == j:
            c = c + 1
    if c > 1:
        print("First repeating character is:", i)
        break