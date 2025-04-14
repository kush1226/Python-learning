"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 06.1 -  math quiz
Date: 03/03/2025

Description:
    The program is to give the user a simple division problem to solve. The program should then allow the user to enter the answer. 

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
import random as r

"""Write new functions below this line (starting with unit 4)."""
def random_factor(num_digit):# random_factor function for generating randint
    if num_digit == 1:
        return r.randrange(1, 10, 1) 
    else:
        return r.randrange(10, 100, 1) 


def main():
    """Write your mainline logic below this line (then delete this line)."""
    one_digit_ran = random_factor(1) 
    two_digit_ran = random_factor(2)

    numerator = one_digit_ran * two_digit_ran
    denominator = one_digit_ran

    answer = int(numerator/denominator) # correct answer

    print(f" {numerator:3d}")
    print(f"÷  {denominator}")
    print("----")

    user_answer = int(input("= "))# user's input answer

    if answer == user_answer:
        print("Great job, that's correct!") #when user has input the correct answer
    else:
        print(f"Sorry, the correct answer is {answer}.") #when user has input the incorrect answer


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
