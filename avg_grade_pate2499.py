"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 04.3 -  avg grade
Date: 02/16/2025

Description:
    The program is to asks the user to enter a valid score five times. The program should display a letter grade after each score is entered. 
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

def get_valid_score():
    while True:
        try:
            score = float(input("Enter a score: "))  # Get user input and convert to float
            if 0 <= score <= 100:
                return score
            else:
                print("  Invalid Input. Please try again.")  # Error message for out-of-range values
        except ValueError:
            print("  Invalid Input. Please try again.")  # Error message for non-numeric values

def calc_average(scores):
    return sum(scores) / len(scores)

def determine_grade(score):
    if score >= 92:
        return 'A'
    elif score >= 82:
        return 'B'
    elif score >= 73:
        return 'C'
    elif score >= 64:
        return 'D'
    else:
        return 'F'

def main():
    scores = []
    for _ in range(5):
        score = get_valid_score()  # Get a valid score from the user
        print(f"  The letter grade for {score:.1f} is {determine_grade(score)}.")
        scores.append(score) # Add score to the list
    
    average = calc_average(scores)  # Calculate average score
    print("\nResults:")
    print(f"  The average score is {average:.2f}.")
    print(f"  The letter grade for {average:.2f} is {determine_grade(average)}.")


if __name__ == "__main__":
    main()

