#Given: text = "knowyourself"
#Print the alternate characters in the given string.

text="knowyourself"
for i in range(0,len(text),2):
    print(text[i],end=" ")