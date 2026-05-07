# Write a script to analyze cricket stats for a team

Player_1 = int(input("Enter runs scored by player_1 :"))
Player_2 = int(input("Enter runs scored by player_2 :"))
Player_3 = int(input("Enter runs scored by player_3 :"))
Player_4 = int(input("Enter runs scored by player_4 :"))
Player_5 = int(input("Enter runs scored by player_5 :"))
Total_runs = Player_1 + Player_2 + Player_3 + Player_4 + Player_5
print(f"Total runs = {Total_runs}")
Average_runs = Total_runs / 5
print(f"Average runs = {Average_runs}")