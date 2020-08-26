import random
play_again = "y"
while play_again == "y":
    random_number = random.randint(1, 10)  # Number 1 - 10
    user_guess = int(input("Guess a number between 1 and 10: "))
    while user_guess != random_number:
        if user_guess < random_number:
            print("Your guess is too low!")
            user_guess = int(input())
        elif user_guess > random_number:
            print("Your guess is too high!")
            user_guess = int(input())
    print("Your guess is correct, the number is: {}".format(random_number))
    play_again = input("Do you want to play again? [y/n] ")

# handle user guesses
#   if they guess correctly, tell them they won
#   otherwise, tell them if they are too high or too low

# Bonus - Let player play again if they want
