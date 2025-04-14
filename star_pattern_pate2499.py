"""
Author:     kush Patel , pate2499@purdue.edu
Assignment: 05.3 - star pattern
Date: 02/24/2025

Description:
    The program is designed to use a loop with turtle graphics to draw a star pattern that has a user specified number of points.This is done for various number of points on the star.

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
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(7)
    side_length = 60 # Inner side of a star 
    penup()
    goto(0, -side_length)  # Start at the bottom of the star.
    pendown()
    color('black', 'pink') #colour of the star


def main():
    """Write your mainline logic below this line (then delete this line)."""
    side_length = 60
    p= int(input('Enter the number of points: ')) #add total number of points on the edge
    A = 360/p
    B = 2*A # Concave angle between star points
    right((180-B)/2) # Inner angle of a star point
    begin_fill()
    for n in range(p):
        forward(side_length)
        left(180-A)
        forward(side_length)
        right(180-B)
    end_fill()

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
