import random

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == "__main__":
    print("    Rock-Paper-Scissors Game!    ")
    print("------------------------------------")

   
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

   
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    
    if user_choice not in choices:
        print("Invalid choice. Please choose from 'rock', 'paper', or 'scissors'.")
    else:
        print(f"You chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

       
        result = winner(user_choice, computer_choice)
        print(result)
