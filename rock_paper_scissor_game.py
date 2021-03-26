import random

while True:
    user_input = input('Kindly enter a choice (rock, paper, scissors): ')

    #list of possible actions
    possible_actions = ["rock", "paper", "scissors"]

    #allow a random element be chosen from the list
    computer_action = random.choice(possible_actions)

    #print the choices that the user and the computer made
    print(f"\nYou chose {user_input}, computer chose {computer_action}.\n")

    #to determine the winner

    if user_input == computer_action:
        print("both players selected {user_input}. It's a tie!")
    elif user_input == 'rock':
        if computer_action == 'scissors':
            print('Rock smashes scissors! You win!')
        else:
            print('Paper covers rock! You lose!')
    elif user_input == 'paper':
        if computer_action == 'rock':
            print('Paper covers rock! You win')
        else:
            print('Scissors cuts paper! You lose!')
    elif user_input == 'scissors':
        if computer_action == 'paper':
            print('Scissors cuts paper! You win!')
        else:
            print('Rock smashes scissors! You lose')
    
    play_again = input('Would you like to play again? (y/n): ')
    if play_again.lower() != 'y':
        break 
        




