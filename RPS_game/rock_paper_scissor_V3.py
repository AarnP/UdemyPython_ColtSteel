# Research about Randint and how to avoid case-sensitive cases
# import random
from random import randint
print("Welcome to RPS advanced game")
player_win = 0
pc_win = 0
player1_choice = ""
while player_win < 2 and pc_win < 2:
    # print("Player score: {} and Computer score: {}".format(player_win, pc_win))
    for time in range(3):
        rand_number = randint(0, 2)
        if rand_number == 0:
            computer_choice = "scissor"
        elif rand_number == 1:
            computer_choice = "paper"
        else:
            computer_choice = "rock"
        print("Player score: {} and Computer score: {}".format(player_win, pc_win))
        if player1_choice == "quit" or player1_choice == "q":
            break
        player1_choice = input("Player 1 chooses: ").lower()  # Player intput
        if player1_choice:  # if player1_choice is valid
            print("Computer plays {}".format(computer_choice))
            # print("Computer plays: " + computer_choice)
            if player1_choice == computer_choice:  # When the choices are similar
                print("It is a tie")
            elif player1_choice == "scissor":
                if rand_number == 1:  # Paper
                    print("Human Player wins")
                    player_win += 1
                elif rand_number == 2:  # Rock
                    print("Computer wins")
                    pc_win += 1
            elif player1_choice == "paper":
                if rand_number == 0:  # Scissor
                    print("Computer wins")
                    pc_win += 1
                elif rand_number == 2:  # Rock
                    print("Human Player wins")
                    player_win += 1
            elif player1_choice == "rock":
                if rand_number == 0:  # scissor
                    print("Human Player wins")
                    player_win += 1
                elif rand_number == 1:  # Paper
                    print("Computer wins")
                    pc_win += 1
        else:
            print("Human Player please enter a valid choice")

if player_win > pc_win:
    print("Congratulation, you won!")
elif player_win == pc_win:
    print("The result is tie!")
else:
    print("The computer achieve Victory!")
print("FINAL SCORE -- Player score: {} and Computer score: {}".format(player_win, pc_win))
