# Write a program that prompts the user for their age and tells them how many years until they reach retirement age (65).

Age = int(input("Enter your age :"))
For_retirement = (65 - Age)
if Age <= 65:
    print(f"you have {For_retirement} years until you reach retirement age.")
else:
    print("you have already reached retirement age")