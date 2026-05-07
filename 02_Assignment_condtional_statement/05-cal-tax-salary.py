#You have to calculate an employee's salary by computing the gross salary tax and net salary based on the given parameters.

Base_salary = 50000
Bonus = 5000
Tax_rate = 10
Other_charges = 2000
gross_salary = Base_salary + Bonus + Other_charges
tax = (Tax_rate / 100) * gross_salary
print(f"Gross Salary Tax = {tax}")
net_salary = gross_salary - tax
print(f"Net Salary = {net_salary}")