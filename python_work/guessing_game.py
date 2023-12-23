import random

# This is a fun guessing game!
# Please play this game!

while True:
    name = input("What is your name?: ")
    your_choice = input("Lets play the guessing game! If you guess the number between 1-10, you get a prize!\nPlease guess a number between 1-10: ")
    your_choice = int(your_choice)
    possible_actions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {your_choice}, computer chose {computer_action}.\n")
    game_host_name = "Anish Pasumarthi"
    
    if your_choice == computer_action:
        print(f"Congrats {name.title()}, You WON the game, run to {game_host_name.title()} to get your prize")
    else:
        print(f"Sorry {name.title()}, you DID NOT win the game.")

    play_again = input("Thanks for playing!\nDo you want to play again? Type 'yes' to play again. Otherwise, type ANYTHING to quit the game.")
    if play_again != 'yes':
        break