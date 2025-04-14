"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 02.2 -  Software sales
Date: 02/01/2025

Description:
    The program is to build a calculator which determines if a package is purchased and if yes, number of packages with applicable discount.
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
#input is the number of packages purchased
 quantity = int(input('How many packages will be purchased: '))
 price = 880 * quantity
 if (quantity <= 0):
  print(f"  Invalid Input!")
  return
 if (quantity <4):
     discount =0
     print(f'  No discount applied.')
     print(f'  The total price to purchase {quantity} packages is ${price:,.2f}.')
 elif (quantity >= 4) and (quantity <= 39):
     print(f'  10% discount applied.')
     print(f'  The total price to purchase {quantity} packages is ${0.9 * price:,.2f}.')
 elif (quantity >= 40) and (quantity <= 199):
     print(f'  15% discount applied.')
     print(f'  The total price to purchase {quantity} packages is ${0.85 * price:,.2f}.')
 elif (quantity >= 200) and (quantity <= 999):
     print(f'  30% discount applied.')
     print(f'  The total price to purchase {quantity} packages is ${0.7 * price:,.2f}.')
 elif (quantity >= 1000):
     print(f'  42% discount applied.')
     print(f'  The total price to purchase {quantity} packages is ${0.58 * price:,.2f}.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
