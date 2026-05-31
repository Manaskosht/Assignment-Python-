#.Count only words not spaces. 
#Entered a string: Hello coders from Success24 
#Number of words: 4 

text = input("Enter a string: ")
words = text.split()   
num_words = len(words)
print("Number of words:", num_words)