"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 04.4 -  prime numbers
Date: 02/16/2025

Description:
    The program is to Write a Boolean function named is_prime which takes an integer as an argument and returns True if the argument is a prime number, or False otherwise.
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

def is_prime(n):
    if n < 2:#Checks if a number is prime.
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:#prime numbers are always positive so make sure that the upper limit is a positive integer
            return False
    return True

def main():
    while True:
        try:
            num = int(input("Enter a positive integer (-1 to quit): "))
            if num == -1:#error if the number is negative
                break #exit when number is negative
            if is_prime(num):
                print(f"  {num} is prime!")
            else:
                print(f"  {num} is not prime.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

