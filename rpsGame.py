import random

# Define choices
choices = ["rock", "paper", "scissors"]

# Initialize scores
user_score = 0
computer_score = 0

# Function to get the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Main game loop
while True:
    print("\nRock, Paper, Scissors Game")
    print("Enter your choice (rock, paper, scissors):")

    # Get user's choice
    user_choice = input("Your choice: ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    # Get computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)

    # Update and display the score
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {user_score}, Computer: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing!")
        break
