"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 02.3 -  roulette colors
Date: 02/02/2025

Description:
    The program is to build a calculator which determines the color of that pocket (either green, red, or black) when we choose a pocket number, and then displays .
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
#input is the number of pocket on the roulette table
  pocket = int(input('Please choose a pocket number: '))
  if (pocket < 0) or (pocket > 36):
         print (f'  Invalid Input!')
  elif pocket == 0:
        print (f'  Pocket number {pocket} is green.')
  elif 1 <= pocket <= 10 or 19 <= pocket <= 28:
     if pocket % 2 == 1:
         print (f'  Pocket number {pocket} is red.')  
     else: 
         print (f'  Pocket number {pocket} is black.')
  elif 11 <= pocket <= 18 or 29 <= pocket <= 36:
     if pocket % 2 == 1:
         print (f'  Pocket number {pocket} is black.')  
     else: 
         print (f'  Pocket number {pocket} is red.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()