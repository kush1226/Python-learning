"""
Author: Kush Patel, login@purdue.edu
Assignment: 07.1 - roll analysis
Date: 03/09/2025

Description:
    This program simulates rolling two six-sided dice 1,000,000 times, calculates the frequency of each possible total (2-12), and prints the percentage distribution in a formatted table.
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

# Function to simulate rolling a single six-sided die
def roll_d6():
    return random.randint(1, 6)

# Function to simulate rolling two six-sided dice multiple times
def get_2d6_rolls(num_rolls):
    return [roll_d6() + roll_d6() for _ in range(num_rolls)]

# Function to analyze the frequency of each roll outcome (2-12)
def analyze_rolls(rolls):
    roll_counts = {i: 0 for i in range(2, 13)}
    
    for roll in rolls:
        roll_counts[roll] += 1
    
    total_rolls = len(rolls)
    percentages = {key: (value / total_rolls) * 100 for key, value in roll_counts.items()}
    
    return percentages

# Main function to run the dice roll simulation and print results
def main():
    num_rolls = 1_000_000
    rolls = get_2d6_rolls(num_rolls)
    percentages = analyze_rolls(rolls)
    
    print("Roll  Frequency")
    for roll in range(2, 13):
        print(f"{roll:>3}    {percentages[roll]:5.2f}%")  # Adjust spacing for formatting

if __name__ == "__main__":
    main()