import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Enter the number of players between 2 to 4")
    else:
        print("Invalid value")

max_score = 50
player_score = [0 for i in range(players)]
print(player_score)

while max(player_score) < max_score:
    for player_ind in range(players):
        print("\nPlayer", player_ind + 1, "turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                current_score = 0
                print("You rolled a 1. Turn done!")
                break
            else:
                current_score += value
                print("You rolled a", value)

        print("Your current score is:", current_score)
        player_score[player_ind] += current_score
        print("Your total score is:", player_score[player_ind])

        if player_score[player_ind] >= max_score:
            break

print("\nGAME OVER!")
print("Scores:", player_score)
winner = player_score.index(max(player_score)) + 1
print("Player", winner, "wins!")

