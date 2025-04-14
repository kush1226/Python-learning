"""
Author: Kush Patel, login@purdue.edu
Assignment: 07.2 - spiral
Date: 03/10/2025

Description:
   This program draws a shrinking spiral by interpolating points along a square's edges using Python's turtle module. The spiral continues until the line length falls below a set threshold.

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

def interpolate_point(p1, p2, t):
    """Returns a point t of the way from p1 to p2."""
    x = p1[0] + t * (p2[0] - p1[0])
    y = p1[1] + t * (p2[1] - p1[1])
    return (x, y)

def draw_square(side_length):
    """Draws a square centered at the origin."""
    penup()
    goto(-side_length / 2, side_length / 2)  # Move to top-left corner
    pendown()
    for _ in range(4):
        forward(side_length)
        right(90)

def main():
    side_length = 200  # Initial square side length
    t = 0.1  # Smaller fraction to interpolate
    min_length = 5  # Minimum line length to stop
    
    # Define square corner points
    p1 = (side_length / 2, side_length / 2)  # Top-right
    p2 = (side_length / 2, -side_length / 2) # Bottom-right
    p3 = (-side_length / 2, -side_length / 2) # Bottom-left
    p4 = (-side_length / 2, side_length / 2) # Top-left

    points = [p1, p2, p3, p4]  # Store square corners
    penup()
    goto(p1)
    pendown()

    width(1)  # Ensure pen width is 1
    
    # Draw spiral
    total_path_length = 0
    prev_point = p1
    while side_length > min_length:
        new_point = interpolate_point(points[0], points[1], t)
        goto(new_point)
        total_path_length += distance(prev_point, new_point)  # Add the distance to the total
        prev_point = new_point
        points.append(new_point)  # Store the new point
        points.pop(0)  # Remove the oldest point

        side_length *= (1 - t)  # Reduce length
    
    print("Total path length:", total_path_length)

if __name__ == "__main__":
    main()
    done()
