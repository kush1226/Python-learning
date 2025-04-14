"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 10.2 - gas prices
Date: 04/06/2025

Description:
    This program reads weekly 2008 U.S. gas prices from a file and plots them as a line graph using matplotlib, with labeled axes, grid, and title saved as a PDF with your Purdue login
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

import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""


def main():

    gas_prices = []
 
    with open("2008_Weekly_Gas_Averages.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line:
                gas_prices.append(float(stripped_line))
    
    weeks = list(range(1, len(gas_prices) + 1)) # Generate week numbers (1 to 52)
    
    fig, ax = plt.subplots()
    plt.plot(weeks, gas_prices)  # Plot the data as a line graph with markers
    
    # Set axis limit
    ax.set_xlim(1, 52)
    ax.set_ylim(1.5, 4.25)
    
    # Add axis labels and title
    ax.set_xlabel("Weeks (by number)")
    ax.set_ylabel("Average Price (dollars/gallon)")
    ax.set_title("2008 Weekly Gas Prices (pate2499)")
    ax.grid()
    
    #plot and show the figure
    plt.savefig("gas_prices_pate2499.pdf")           
    plt.show()                                      


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
