"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 11.1 - dice
Date: 04/13/2025

Description:
    The program simulates dice rolls using a class with customizable sides. Rolls each die 10 times and prints the results in a formatted output.
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

class Dice:
    def __init__(self, sides):
        self.sides = sides #the number of sides of the dice

    def roll(self):
        return random.randint(1, self.sides) #to determine the range of the roll from 1 to total no of sides in the dice.

    def n_rolls(self, n):
        results = [str(self.roll()) for _ in range(n)] #to determine the number of the roll from for the dice.
        print(f"Rolling a {self.sides} sided die {n} times: {', '.join(results)}") #printing the output

def main():
    d6 = Dice(6)
    d10 = Dice(10)
    d20 = Dice(20)

    d6.n_rolls(10)
    d10.n_rolls(10)
    d20.n_rolls(10)

if __name__ == "__main__":
    main()
