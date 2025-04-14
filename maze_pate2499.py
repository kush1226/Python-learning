"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 05.1 - Assignment Namemaze
Date: 02/24/2025

Description:
    this code is to make a path in a maze using turtle graphics. there can be multiple path and main objective is to escape the maze starting from centre

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

import os
from turtle import *

"""Write new functions below this line (starting with unit 4)."""

def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    bgpic(os.path.join("D:\purdue\IE courses\sem 2\EBEC\WEEK 5\maze", "maze.png"))
    shape("turtle")
    color("green")
    width(5)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    speed(0) # Adjust speed as needed
    forward(13)#step 1 in the movemement
    right(90)
    forward(60)
    right(90)
    forward(25)
    left(90)
    forward(25)
    right(90)
    forward(48)
    left(90) 
    forward(25)
    right(90)
    forward(147)
    right(90)
    forward(100)
    left(90)
    forward(20)
    right(90) 
    forward(240)
    right(90)
    forward(455)
    right(90)
    forward(230)
    left(90)
    forward(20)


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
