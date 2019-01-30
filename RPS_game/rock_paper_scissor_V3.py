# Research about Randint and how to avoid case-sensitive cases
# import random
from random import randint
print("Welcome to RPS advanced game")
rand_number = randint(0, 2)
if rand_number == 0:
    computer_choice = "scissor"
elif rand_number == 1:
    computer_choice = "paper"
else:
    computer_choice = "rock"
player1_choice = input("Player 1 chooses: ").lower()  # Player intput
if player1_choice:  # if player1_choice is valid
    print("Computer plays {}".format(computer_choice))
    # print("Computer plays: " + computer_choice)
    if player1_choice == computer_choice:  # When the choices are similar
        print("It is a tie")
    elif player1_choice == "scissor":
        if rand_number == 1:  # Paper
            print("Human Player wins")
        elif rand_number == 2:  # Rock
            print("Computer wins")
    elif player1_choice == "paper":
        if rand_number == 0:  # Scissor
            print("Computer wins")
        elif rand_number == 2:  # Rock
            print("Human Player wins")
    elif player1_choice == "rock":
        if rand_number == 0:  # scissor
            print("Human Player wins")
        elif rand_number == 1:  # Paper
            print("Computer wins")
else:
    print("Human Player please enter a valid choice")
