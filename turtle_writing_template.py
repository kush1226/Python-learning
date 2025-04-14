"""
Author: Your Name, login@purdue.edu
Assignment: mm.n - Assignment Name
Date: MM/DD/YYYY

Description:
    Describe your program here.

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

def start():
    setup(800, 400)
    width(9)
    color("purple")
    speed(3)

def move_to(x, y):
    penup()
    goto(x, y)
    pendown()

def draw_S():
    move_to(-300, 100)
    setheading(0)
    circle(30, 180)
    circle(-30, 180)

def draw_t():
    move_to(-220, 130)
    setheading(-90)
    forward(80)
    move_to(-240, 130)
    setheading(0)
    forward(40)

def draw_e():
    move_to(-150, 100)
    setheading(0)
    circle(25, 300)

def draw_p():
    move_to(-80, 50)
    setheading(90)
    forward(60)
    circle(20, 180)

def draw_L():
    move_to(-250, -50)
    setheading(-90)
    forward(80)
    left(90)
    forward(40)

def draw_o():
    move_to(-150, -70)
    setheading(0)
    circle(25)

def draw_a():
    move_to(-80, -60)
    setheading(60)
    forward(40)
    right(120)
    forward(40)
    move_to(-65, -30)
    setheading(-90)
    forward(20)

def draw_Small_s():
    move_to(0, -60)
    setheading(0)
    circle(15, 180)
    circle(-15, 180)

def draw_T():
    move_to(50, 130)
    setheading(-90)
    forward(80)
    move_to(30, 130)
    setheading(0)
    forward(40)

def main():
    draw_S()
    draw_t()
    draw_e()
    draw_p()
    draw_Small_s()
    move_to(20, 50)  # Space between words
    draw_T()
    draw_o()
    move_to(-250, -50)  # Space before "Leaps"
    draw_L()
    draw_e()
    draw_a()
    draw_p()
    draw_Small_s()

if __name__ == "__main__":
    start()
    main()
    done()
