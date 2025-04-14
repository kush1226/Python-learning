"""
Author: Kush, pate2499@purdue.edu
Assignment: 01.2 -  Interest
Date: 01/22/2025

Description:
    The program is about calculating the future value (the amount of money in the account after the specified number of years) of an investment.

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
    print('Enter the following parameters.')
    p = float(input('  The initial deposit? '))
    r = float(input('  The annual interest rate in percent? '))/100 #converting the percentage into decimal 
    t = float(input('  The number of years the account earn interest? '))
    n = float(input('  The number of times interest is compounded each year: '))
    
    #calculation of cost based on input variables
    f_v = p * (1+ r/n) ** (n*t)
    #generated output
    print(f'The balance of this account will be ${f_v:,.2f} after {t:.1f} years.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()