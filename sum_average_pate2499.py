"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 03.2 -  sum average
Date: 02/07/2025

Description:
    The program is to to enter non-negative numbers and display their sum and average.
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
#input a number non-negative
 count = 0
 total = 0.0

 num = float(input("Enter a non-negative number (negative to quit): "))
 while num >= 0:
     count += 1
     total += num
     num = float(input("Enter a non-negative number (negative to quit): "))

 if count == 0: #ends if the number entered is negative
     print("  You didn't enter any numbers.")
 else:
     print(f"  You entered {count} numbers.")
     print(f"  Their sum is {total:.3f} and their average is {total / count:.3f}.") #can add an average function or calculate directly

     
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
