# zuri task: create a rock paper scissors game
import random
plays = ["rock", "paper", "scissors"]
rounds_played = 0
player_points = 0
computer_points = 0


def computer_play():
    # this function generates a random choice for the computer
    computer_play = random.choice(plays)
    return computer_play


def compare(computer, player):
    # the compare function is responsible for evaluating who the winner is
    # it returns a boolean tie, tie has a default value of false
    # however if the players tie its value is set to true
    # compare function is also responsible for displaying the results of a game
    tie = False
    global computer_points, player_points, rounds_played
    print("----------------------------")
    print("", player_name, "("+player+")", "\n CPU ", "("+computer+")")
    if computer == player:
        print(" TIE!!!")
        tie = True
    else:
        if computer == 'rock':
            if player == 'scissors':
                print(" COMPUTER WINS!!! ")
                computer_points += 1
            else:
                print("", player_name, " WINS!!! ")
                player_points += 1
        elif computer == "paper":
            if player == "rock":
                print(" COMPUTER WINS!!! ")
                computer_points += 1
            else:
                print("", player_name, " WINS!!! ")
                player_points += 1
        else:
            if player == "paper":
                print(" COMPUTER WINS!!! ")
                computer_points += 1
            else:
                print("", player_name, " WINS!!! ")
                player_points += 1

    rounds_played += 1
    print("----------------------------")
    print(" SCORES", "\n Computer:", computer_points,
          "\n " + player_name, player_points)
    print(" Rounds played:", rounds_played)
    print("----------------------------")
    return tie


print("This is a game of rock paper scissors")
player_name = input("Enter player name: ")
play = True

while(play):
    print("\nplease choice between the following options",
          "\n\nR for rock", "\n\nP for paper", "\n\nS for scissors\n")

    player_input = input("Enter: ")
    if player_input == "R":
        player_choice = "rock"
    elif player_input == "P":
        player_choice = "paper"
    elif player_input == "S":
        player_choice = "scissors"
    else:
        print("\nERROR you have picked and invalid option")
        continue
    computer_choice = computer_play()
    if compare(computer_choice, player_choice):
        print("A TIE HAS OCCURED")
        continue
    play = input("would you like to play again y/n: ")
    if play.lower() == "y":
        play = True
    else:
        play = False
