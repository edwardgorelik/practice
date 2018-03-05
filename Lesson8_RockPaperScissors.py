import random
#take the player input and start the game
play = "y"

#create the loop that occurs for the game
while play == "y":
    player = input("Rock, Paper, or Scissors?")
    a = ["Rock", "Paper", "Scissors"]
    a = a[random.randint(0,2)]
    print("Your opponent got ", a)
    if a == "Scissors":
        if player == "Rock":
            print("Player Wins")
        if player == "Scissors":
            print("Tie Game")
        if player == "Paper":
            print("Player Lost")
    elif a == "Rock":
        if player == "Rock":
            print("Tie Game")
        if player == "Scissors":
            print("Player Lost")
        if player == "Paper":
            print("Player Wins")
    elif a == "Paper":
        if player == "Rock":
            print("Player Lost")
        if player == "Scissors":
            print("Player Wins")
        if player == "Paper":
            print("Tie Game")
    play = input("Do you want to play again y/n?")