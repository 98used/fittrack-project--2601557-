player_name = input("enter the player name : ")
no_of_games_played = int(input("give the no of games : "))
score = int(input("total score : "))
average_score = float(score/no_of_games_played)

print(f"Player: <",{player_name},">")
print(f"Games Played: <",{no_of_games_played},">")
print(f"Total Score: <",{score},">")
print(f"Average Score: <",{average_score},">")
