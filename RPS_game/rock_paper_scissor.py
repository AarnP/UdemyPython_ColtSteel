print("Welcome to RPS basic game")
option1 = "scissor"
option2 = "paper"
option3 = "rock"
player1_choice = input("PLayer 1 chooses: ")
player2_choice = input("PLayer 2 chooses: ")
if player1_choice and player2_choice:
    print("SHOOT!")
    if player1_choice == option1 and player2_choice == option2:
        print("Player 1 Win")
    elif player1_choice == option2 and player2_choice == option3:
        print("Player 1 Win")
    elif player1_choice == option3 and player2_choice == option1:
        print("Player 1 Win")
    elif player1_choice == player2_choice:
        print("It is a tie")
    else:
        print("PLayer 2 Win")
else:
    print("Player please enter your choice")
