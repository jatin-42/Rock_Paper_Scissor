import random

def get_choices():
    player_choice = input("Enter a choice ('rock', 'paper', or 'scissor'): ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice.lower(), "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player} and the computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissor":
            return "Rock smashes scissor! You win!"
        else:
            return "Paper covers rock! You lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissor cuts paper! You lose!"
    elif player == "scissor":
        if computer == "rock":
            return "Rock smashes scissor! You lose!"
        else:
            return "Scissor cuts paper! You win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
