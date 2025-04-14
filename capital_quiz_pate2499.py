"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 09.1 - capital quiz
Date: 03/30/2025

Description:
    This program reads steps.txt, calculates the average daily steps for each month in a non-leap year, and displays results with set decimal precision, ensuring output format matches the provided sample exactly.
    
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


"""Write new functions below this line (starting with unit 4)."""
def get_state_data():
    with open("state_capitals.txt", "r") as file:
        lines = file.readlines()

    state_capitals = {}  # Creating a word dictionary from the lines
    for line in lines:
        capital, state = line.rsplit(", ")
        state_capitals[state.strip()] = capital.strip()

    return state_capitals # return the dict


def main():

    state_capitals = get_state_data()

    states = list(state_capitals.keys())
    random.shuffle(states)  # Randomizing the state order in the list
    
    incorrect_states = []   # states that were answered incorrectly
    correct_count = 0  # states that were answered correctly
    total_attempts = 0   # counting the total number of attempts
    
    while states:
        state = states.pop()
        capital = state_capitals[state]
        
        user_input = str(input(f"What is the capital of {state} (enter 0 to quit)? "))
        
        if user_input == "0":
            break # Exit the quiz when the user enters 0

        total_attempts += 1

        if user_input.lower() == capital.lower():   # Case-insensitive check
            print("  That is correct!")
            correct_count += 1
        else:
            print("  That is incorrect.")
            print(f"  The capital of {state} is {capital}.")
            incorrect_states.append(state)# Add to incorrect list

        if not states:  # If main list is empty, refill with incorrect states
            states.extend(incorrect_states)
            incorrect_states = []

    if total_attempts == 0:
        print("You didn't answer any questions.")
    else:
        accuracy = (correct_count / total_attempts) * 100
        print(f"You answered {accuracy:.1f}% of the questions correctly.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

