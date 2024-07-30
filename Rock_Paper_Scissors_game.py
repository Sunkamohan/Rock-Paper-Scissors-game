import random

def get_user_choice():
    """
    Prompt the user to enter their choice and return it.

    Returns:
        str: The user's choice (rock, paper, or scissors).
    """
    while True:
        print("\nEnter your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            return 'rock'
        elif choice == '2':
            return 'paper'
        elif choice == '3':
            return 'scissors'
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """
    Randomly select the computer's choice and return it.

    Returns:
        str: The computer's choice (rock, paper, or scissors).
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the user's and computer's choices.

    Args:
        user_choice (str): The user's choice (rock, paper, or scissors).
        computer_choice (str): The computer's choice (rock, paper, or scissors).

    Returns:
        str: The result of the game (win, lose, or tie).
    """
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        return 'lose'

def print_result(result, user_choice, computer_choice):
    """
    Print the result of the game.

    Args:
        result (str): The result of the game (win, lose, or tie).
        user_choice (str): The user's choice (rock, paper, or scissors).
        computer_choice (str): The computer's choice (rock, paper, or scissors).
    """
    print(f"\nYou chose {user_choice}. The computer chose {computer_choice}.")
    if result == 'win':
        print("You win!")
    elif result == 'lose':
        print("You lose.")
    else:
        print("It's a tie.")

def main():
    """
    Main function to run the Rock Paper Scissors game.

    This function handles the game loop, user input, and determines the game result.
    """
    while True:
        print("\nRock Paper Scissors Game")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print_result(result, user_choice, computer_choice)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thank you for playing! Goodbye.")
            break

if __name__ == '__main__':
    main()
      
