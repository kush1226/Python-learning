"""
Author: Kush Patel, login@purdue.edu
Assignment: 07.4 - magic square
Date: 03/09/2025

Description:
    This program checks if a 3*3 grid is a Lo Shu Magic Square by verifying it contains numbers 1-9 and that all rows, columns, and diagonals sum to 15. It prints the grid and outputs the result.
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

"""
Author: Kush Patel, login@purdue.edu
Assignment: 07.4 - magic square
Date: 03/09/2025

Description:
    This program checks if a 3*3 grid is a Lo Shu Magic Square by verifying it contains numbers 1-9 and that all rows, columns, and diagonals sum to 15. It prints the grid and outputs the result.
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

def print_square(square):
    """Prints the 3x3 square in a formatted manner."""
    for row in square:
        print(" ", " ".join(map(str, row)))

def is_magic(square):
    """Checks if the given 3x3 square is a Lo Shu Magic Square."""
    magic_sum = 15  # The sum for each row, column, and diagonal in a Lo Shu Magic Square
    
    # Check if it contains exactly numbers 1-9
    numbers = {num for row in square for num in row}
    if numbers != set(range(1, 10)):
        return False
    
    # Check rows and columns sum
    for i in range(3):
        if sum(square[i]) != magic_sum:  # Row sum
            return False
        if sum(square[j][i] for j in range(3)) != magic_sum:  # Column sum
            return False
    
    # Check diagonals sum
    if sum(square[i][i] for i in range(3)) != magic_sum:
        return False
    if sum(square[i][2 - i] for i in range(3)) != magic_sum:
        return False
    
    return True

def main():
    squares = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    ]
    
    for square in squares:
        print('Your square is:')  # Print square label
        print_square(square)  # Print the square itself
        if is_magic(square):
            print("It is a Lo Shu magic square!")  # If the square is magic, print this
        else:
            print("It is not a Lo Shu magic square.")  # Otherwise, print this
            print()  # Print a blank line for spacing between squares


if __name__ == "__main__":
    main()
