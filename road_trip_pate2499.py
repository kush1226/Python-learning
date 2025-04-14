"""
Author: Kush, pate2499@purdue.edu
Assignment: 01.1 -  Road Trip
Date: 01/21/2025

Description:
    The program is about calculating the cost of road trip

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
    #input
    print('Road trip fuel cost estimator:')
    d = float(input('  How far away is your destination (miles)? '))
    p = float(input('  What is the average price of gas (dollars per gallon)? '))
    mpg = float(input('  What is the fuel efficiency of your vehicle (mpg)? '))
    #calculation of cost based on input variables
    fuel_cost = int((2 * d * p) / mpg)
    
    #generated output
    print()
    print(f'The fuel cost for this trip is approximately ${fuel_cost}.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()