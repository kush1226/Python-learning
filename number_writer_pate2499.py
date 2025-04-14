"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 08.4 - number writer
Date: 03/17/2025

Description:
    This program generates a user-specified number of random integers within a given range, excluding numbers whose digits sum to 13, and writes them to random_numbers.txt, ensuring randomness and validity.
    
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
import random

"""Write new functions below this line (starting with unit 4)."""
def sum_of_digits(n):
    total = 0
    for digit in str(n):  # Convert number to string and iterate over each digit
        total += int(digit)  # Convert digit back to integer and add to total sum
    return total

def generate_random_numbers(count):
    filename = "random_numbers.txt"
    valid_numbers = []

    for num in range(1119, 1218):  # Generate numbers from 1119 to 1217 (inclusive)
        if sum_of_digits(num) != 13:
            valid_numbers.append(num)  # Store numbers where the sum of digits is not 13

    with open(filename, "w") as file:
        for _ in range(count):
            number = random.choice(valid_numbers)  # Select a random number from valid numbers list
            file.write(f"{number}\n")  # Write each selected number to the file

def main():
    num_count = int(input("How many numbers should be written to `random_numbers.txt`? "))
    generate_random_numbers(num_count)  # Call function to generate and write numbers to file

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
