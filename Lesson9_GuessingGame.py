import random

# does the user want to keep playing
def gameon():
    choice = str(input("Do you want to play again? [y/n]: "))
    if choice.lower() == 'y':
        lets_play()
    else:
        print("That sucks to hear")
        print("..................")
        print("Kind of thought we'd play a game")

# the game itself
# what did the user pick
# what was the number
# how did the user do in guessing that number?
# how many times did the user take to guess the number?
def lets_play():
    computer = random.randint(1,9)
    choice = 0
    tries = 1
    while choice != computer:
        try:
            choice = int(input("Pick a number between 1 and 9"))
        except ValueError:
            print("That's not a number!")
            lets_play()
        if choice == computer:
            print("You got it!")
            print("It took you", tries, "tries to get the correct answer")
            gameon()
        if choice < computer:
            print("Too low")
            tries = tries + 1
        if choice > computer:
            print("Too high")
            tries = tries + 1

lets_play()