print("Welcome to RPS slight improved game")
option1 = "scissor"
option2 = "paper"
option3 = "rock"
player1_choice = input("PLayer 1 chooses: ")
print("NO CHEATING!!\n" * 20)  # Print No cheating on a new line 20 times
player2_choice = input("PLayer 2 chooses: ")
if player1_choice and player2_choice:  # if player1_choice and player2_choice is
                                        # valid input
    print("SHOOT!")
if player1_choice == player2_choice:  # if it is tie, we dont need to check other
    print("It is a tie")
elif player1_choice == option3:  # Rock
    if player2_choice == option1:  # Scissor
        print("PLayer 1 wins")
    elif player2_choice == option2:  # paper
        print("Player 2 wins")
elif player1_choice == option2:  # paper
    if player2_choice == option3:  # rock
        print("Player 1 wins")
    elif player2_choice == option1:  # Scissor
        print("Player 2 wins")
elif player1_choice == option1:  # Scissor
    if player2_choice == option2:  # paper
        print("Player 1 wins")
    if player2_choice == option3:  # Rock
        print("Player 2 wins")
else:
    print("Player please enter a valid choice")
