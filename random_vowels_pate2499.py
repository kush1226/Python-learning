"""
Author: Your Name, login@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 03/03/2025

Description:
    Define vowel-drawing functions in vowels.py and call them in random order in random_vowels_template.py.

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

from turtle import *
import random
import vowels  # Assuming vowels is a separate module that includes the drawing functions

def main():
    # List of vowel drawing functions from the vowels module
    vowel_functions = [vowels.draw_a, vowels.draw_e, vowels.draw_i, vowels.draw_o, vowels.draw_u]
    
    # Shuffle the list to ensure random order at runtime
    random.shuffle(vowel_functions)  
    
    # Iterate over the shuffled list and call each function to draw the vowels
    for func in vowel_functions:
        func()

if __name__ == "__main__":
    # Initialize the turtle graphics window
    vowels.start()
    
    # Run the main function to draw the vowels in random order
    main()
    
    # Finish drawing and close the window when done
    done()
