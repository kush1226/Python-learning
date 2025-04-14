"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 02.5 -  fluid mechanics
Date: 02/02/2025

Description:
    The program is to build a calculator which determines the value of reynolds number based on velocity, diameter and kinematic viscosity.
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


def main():
#input is the temprature, velocity and diameter of pipe to calculate reynolds number
 temp = int(input('Enter the temperature in °C as 5, 20, or 50: '))
 if (temp == 5):
    k= 1.52e-6
 elif (temp == 20): 
    k= 1e-6
 elif (temp == 50):
    k= 5.54e-7
 v = float(input('Enter the velocity of water in the pipe (m/s): '))
 d = float(input("Enter the pipe's diameter (m): "))
 r = (v * d) / k
 print(f'At {temp}.0°C, the Reynolds number for flow at {v} m/s in a {d} m diameter pipe is {r:.2e}.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()