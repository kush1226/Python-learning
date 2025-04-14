"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 04.1 -  falling
Date: 02/07/2025

Description:
    The program is to to enter that accepts an objects falling time  as an argument, and then calculates and returns the distance in meters that the object will fall during that time.
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

def falling_dist(time):
     gravity = 8.87  # Mean surface gravity of Venus in m/s^2
     return float(0.5 * gravity * time ** 2)
 
def main():
     print('Time (s)  Distance (m)')
     print('----------------------')
     
     for time in range(5, 55, 5):  # Loop from 5 to 50 in increments of 5
         distance = falling_dist(time)
         print(f"{time:>8}  {distance:>12.1f}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
