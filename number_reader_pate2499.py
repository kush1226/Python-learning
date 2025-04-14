"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 08.5 - number reader
Date: 03/20/2025

Description:
    This program reads random numbers from random_numbers.txt and calculates the count, minimum, maximum, sum, and average. It then displays the results, ensuring the output format matches the given sample exactly.
    
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
def read_random_numbers(filename):

    numbers = [] # starting with an empty list to append numbers

    with open(filename, "r") as file:
        for line in file:
            numbers.append(int(line.strip()))   # Converting each line to an integer and adding to the list

    total_numbers = len(numbers) # total of all numbers
    min_number = min(numbers) # minimum number
    max_number = max(numbers)  # maximun number
    sum_numbers = sum(numbers) # sum of all the numbers
    avg_number = sum_numbers / total_numbers  # average of all the numbers

    print(f"{total_numbers:,} numbers were read from the file.")
    print(f"Min: {min_number:,}")
    print(f"Max: {max_number:,}")
    print(f"Sum: {sum_numbers:,}")
    print(f"Avg: {avg_number:,.1f}")



def main():
    filename="random_numbers.txt"              
    read_random_numbers(filename) # calling the numbers from file


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()


