#.You are managing a simple banking system that tracks the balance at the end of 
#each day over 10 days. Each day, the balance increases by 100 units starting from 100 
#on day 1, 200 on day 2, and so on. You want to print the current day’s balance along with 
#the previous day’s balance. For day 1, the previous day’s balance is 0. 

previous_balance = 0
for day in range(1, 11):
    current_balance = day * 100
    print(f"Day {day}: Previous Balance = {previous_balance}, Current Balance = {current_balance}")
    previous_balance = current_balance