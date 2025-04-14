"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 03.1 -  Cakes
Date: 02/07/2025

Description:
    The program is to to enter a number of layers, and then uses nested loops to draw the ASCII art cake pattern from star symbol.
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
#input a number which corresponds to number of layers of cake
 l = int(input('Enter the number of layers: '))
 for i in range(1, l + 1):
        spaces = ' ' * (l - i)  # to center align the spaces
        stars = ''
        
        # Inner loop to construct the stars
        for j in range(2 * i - 1):
            stars += '*'
        
        print(f"{spaces}[{stars}]")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
