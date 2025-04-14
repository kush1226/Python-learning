"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 06.2 -  rock paper scissors
Date: 03/02/2025

Description:
 The program is to Write a program that lets the user play a game of Rock, Paper, Scissors against the computer. You choose one of these and computer chosses other to decide the winner.   
Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""

import random

def get_computer_choice():
    """Randomly selects and returns the computer's choice."""
    return random.choice(["rock", "paper", "scissors"])

def get_player_choice():
    """Prompts the player for input and ensures a valid choice is made."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()  # user enters any of the given input here
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("You made an invalid choice. Please try again.")

def get_winner(computer_choice, player_choice):
    """Determines the winner based on the game rules."""
    if computer_choice == player_choice:
        return "tie"
    elif (
        (computer_choice == "rock" and player_choice == "scissors") or
        (computer_choice == "scissors" and player_choice == "paper") or
        (computer_choice == "paper" and player_choice == "rock")
    ):
        return "computer" # computer wins in other cases
    else:
        return "player" # Player wins in other cases

def main():
    """Runs the Rock, Paper, Scissors game."""
    while True:
        computer_choice = get_computer_choice() # Get choices from computer and player
        player_choice = get_player_choice()
        print(f"  The computer chose {computer_choice}, and you chose {player_choice}.")
        
        winner = get_winner(computer_choice, player_choice) # Determine the winner
        
        if winner == "tie":  # Handle tie cases
            print("  It's a tie. Starting over.\n")
            continue
        elif winner == "player": # Display results based on the winner
            print(f"  {player_choice} beats {computer_choice}")
            print("  You won the game!")
        else:
            print(f"  {computer_choice} beats {player_choice}")
            print("  You lost.  Better luck next time.")
        
        print("Thanks for playing.")
        break

if __name__ == "__main__":
    main()
