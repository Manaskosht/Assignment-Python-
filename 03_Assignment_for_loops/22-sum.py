#Given a string text = "python", calculate the sum of the indices of its characters without using the range() or len() functions.

text = "python"
sum = 0
idx = 0
for ch in text:
    sum = sum + idx
    idx = idx + 1
print("Sum of indices =", sum)