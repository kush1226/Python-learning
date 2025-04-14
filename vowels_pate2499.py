"""
Author: Your Name, login@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 03/03/2025

Description:
    Define vowel-drawing functions in vowels.py and call them in random order in random_vowels_template.py.

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
from turtle import *

def draw_a():
    """
    Draw the letter 'A' using turtle graphics.
    """
    # letter A in turtle graphics.
    penup()
    goto(-50, 0)
    pendown()
    circle(20)
    penup()
    goto(-60, -10)
    pendown()
    goto(-40, -10)

def draw_e():
    """
    Draw the letter 'E' using turtle graphics.
    """
     # letter E in turtle graphics
    penup()
    goto(0, 0)
    pendown()
    circle(20, 270)
    penup()
    goto(0, -20)
    pendown()
    goto(10, -20)

def draw_i():
    """
    Draw the letter 'I' using turtle graphics.
    """
     # letter I in turtle graphics
    penup()
    goto(50, 10)
    pendown()
    goto(50, -20)
    penup()
    goto(50, 30)
    pendown()
    dot(5)

def draw_o():
    """
    Draw the letter 'O' using turtle graphics.
    """
     # letter O in turtle graphics
    penup()
    goto(100, 0)
    pendown()
    circle(20)

def draw_u():
    """
    Draw the letter 'U' using turtle graphics.
    """
    # letter U in turtle graphics
    penup()
    goto(150, 10)
    pendown()
    goto(150, -20)
    goto(170, -20)
    goto(170, 10)

def start():
    """
    Set up the turtle graphics environment.
    """
     # SETTING UP THE turtle graphics
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)

