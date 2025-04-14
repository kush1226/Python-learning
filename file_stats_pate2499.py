"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 08.3 - File Stats
Date: 03/21/2025

Description:
    The program inputs data from the given file, counts lines in a text file, counts words per line, totals all words, calculates the average words per line, and prints the file stats.
    
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
    filename = 'frontiero_v_richardson.txt'
    
    # Initialize counters for total words and total lines
    total_words = 0
    total_lines = 0

    with open(filename , 'r') as file:  # Open the file in read mode          
        for line in file:  
            words_list = line.split()  # Split the line into words
            if words_list:  # Check if the line is not empty
                total_lines += 1  # Increment the line count
                total_words += len(words_list)  # Add the word count of the line

    # Calculate the average words per line, avoiding division by zero
    if total_lines > 0:
        average_words_per_line = total_words / total_lines    
    else:
        average_words_per_line = 0

    print(f"Total number of words: {total_words}")
    print(f"Total number of lines: {total_lines}")             
    print(f"Average number of words per line: {average_words_per_line:.1f}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
