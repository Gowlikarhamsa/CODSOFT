import random

while True:
    user_action = input("Choose rock, paper, scissors: ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYour choice: {user_action}, computer choice: {computer_action}.\n")

    if user_action == computer_action:
        print( "t's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print(" You win!")
        else:
            print(" You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print(" You win!")
        else:
            print(" You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print(" You win!")
        else:
            print(" You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
