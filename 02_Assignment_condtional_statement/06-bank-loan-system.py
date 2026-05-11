# Objective: You have to create a javascript script that checks whether an user is eligible for a bank loan based on various criteria.

name = input("Enter your name : ")
nationality = input ("Enter your nationality : ")
age = int(input("Enter your age : "))
income = int(input("Enter your monthly income : "))
credit_score = int(input("Enter your credit score : "))
debt = int(input("Enter your outstanding Debt : "))
if name  and nationality == "indian" and age >= 18 and age <=60 and income >= 25000 and credit_score >= 700 and debt <= 10000 :
   print("Congratulation Loan Approved") 
else :
   print("Loan Rejected")   