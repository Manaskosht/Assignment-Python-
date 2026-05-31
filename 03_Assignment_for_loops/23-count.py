#Given: text = "python programming" Goal: Count how many vowels are in the string. Constraint: Do not use indexing (text[i]) or slicing (text[:]

text = "Python programming"
c=0
for ch in text :
   if ch in "aeiou":
      c+=1
print("Number of vowels :" ,c)