"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 02.1 -  Leap Year
Date: 02/01/2025

Description:
    The program is to build a calculator which determines weather the year entered is leap or not and how many days does the february of that year have!

Contributors:
    Kush Patel, pate2499@purdue.edu [repeat for each]

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
#input is the present year
 year = int(input('Enter a year: '))
 if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f'The year {year} is a leap year.')#if the year is leap
    print(f'February of {year} has 29 days.')
 else:
    print(f'The year {year} is not a leap year.')#if the year is not leap
    print(f'February of {year} has 28 days.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
