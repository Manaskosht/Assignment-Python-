#.Count how many digits in the string are greater than 5 from text = "1234567890".
text = "1234567890"
c=0
for i in text:
    if int(i)>5:
        c=c+1
print(c)