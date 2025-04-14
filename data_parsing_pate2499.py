"""
Author: Kush Patel, login@purdue.edu
Assignment: 07.1 - data parsing
Date: 03/10/2025

Description:
    To write a program that imports gas price data from data.py, processes it to compute the average inflation-adjusted price per gallon for each decade, and displays the results in a formatted table. No input required.
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
    """Main function to calculate and display average prices by decade."""
    
    from data import data  # Importing data 
    print('          :  Price')
    print('  Decade  : in 2021')
    print('          : Dollars')
    print('-------------------')

    # List of tuples containing the start and end indices for each decade in the data list
    decades = [
        (3, 40), (43, 80), (83, 120), 
        (123, 160), (163, 200), (203, 240),
        (243, 280), (283, len(data))  # The last decade may not have a full 10 years
    ]
    
    # Corresponding decade labels
    years = [
        "1950-1959", "1960-1969", "1970-1979",
        "1980-1989", "1990-1999", "2000-2009",
        "2010-2019", "2020-2029"
    ]
    
    # Iterating over decades to calculate and print the average price for each
    for i, (start, end) in enumerate(decades):
        # Calculate the average price using every 4th data point within the given range
        avg = sum(data[start:end:4]) / (10 if i < 7 else 2)  # Adjusting divisor for last decade
        print(f'{years[i]} :  ${avg:.3f}')  # Print decade and formatted average price

"""Do not change anything below this line."""
if __name__ == "__main__":
    main() 
