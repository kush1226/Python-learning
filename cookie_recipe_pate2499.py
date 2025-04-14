"""
Author: Kush, pate2499@purdue.edu
Assignment: 01.3 -  Cookie Recipe
Date: 01/23/2025

Description:
    The program is about calculating the amount of ingriedents a user would need to make a particular number of cookies.

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
    butter = 2.25 / 48 
    sugar = 1.5 / 48 
    flour = 2.5 / 48 

    #print the part  
    cookies = int(input('How many cookies do you want to make? '))

    #ingriendents needed
    butter_needed = butter * cookies #butter needed for cookies
    sugar_needed = sugar * cookies #sugar needed for cookies
    flour_needed = flour * cookies #flour needed for cookies

    print(f'To make {cookies:,} cookies, you will need:')
    print(f'{butter_needed:10,.2f} cups of butter')
    print(f'{sugar_needed:10,.2f} cups of sugar')
    print(f'{flour_needed:10,.2f} cups of flour')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()