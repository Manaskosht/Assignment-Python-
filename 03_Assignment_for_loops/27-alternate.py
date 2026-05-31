# Print the alternate words
#Constraint: Do not use space between words more than onc

text="if you think you can do not do,you can not show think wisely"
text=text.split()
for i in range(0,len(text),2):
    print(text[i],end=" ")