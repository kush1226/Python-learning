"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 04.5 -  prime list
Date: 02/07/2025

Description:
    The program is to lists all the primes starting from 2 up to a user specified limit which is 101 and 30.
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
    if n < 2: #Checks if a number is prime.
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_primes(limit):
    primes = [str(i) for i in range(2, limit + 1) if is_prime(i)] #this is to create a list of prime numbers as strings and calling them in main.
    return ", ".join(primes)

def main():
    try:
        limit = int(input("Enter a positive integer: "))
        if limit < 1:#prime numbers are always positive so make sure that the upper limit is a positive integer

            print("Please enter a positive integer.")
            return
        print(f"The primes up to {limit} are: {list_primes(limit)}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.") #error if the number is negative
if __name__ == "__main__":
    main()

