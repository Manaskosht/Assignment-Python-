#Students Interview Eligibility Checker

academic_percentage = float(input("Enter your academic percentage : "))
attendence_percentage = float(input("Enter your attendence percentage : "))
extracurricular_activity = input("participated extracurricular activities? yes/no : ")
if academic_percentage >= 60 and attendence_percentage >= 75 and  extracurricular_activity == "yes" :
   print("Eligible for Interview")
else:
   print("Not Eligible for Interviews")