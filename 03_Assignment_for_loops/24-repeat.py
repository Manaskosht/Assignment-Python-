#Given: text = "programming"  Goal: Print all characters that repeat in the string

text = "programming"
for i in text:
    c=0
    for j in text:
        if i == j:
            c+=1
    if c > 1:
        print(i)