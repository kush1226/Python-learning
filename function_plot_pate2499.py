"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 10.4 - function plot
Date: 04/06/2025

Description:
    This Program plots two functions with LaTeX-style labels, a custom legend, and formatted ticks, saving the result as a PDF with the user's Purdue login in the filename.

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
import numpy as np

"""Write new functions below this line (starting with unit 4)."""


def main():

    # Create the x values from 0 to 2*pi
    x = np.linspace(0, 2 * np.pi, 400)

    # Define the given functions
    y1 = (3 * np.cos(x))**2 + 1
    y2 = 2 * np.sin(x**2) + 5 * x - 15

    fig, ax = plt.subplots()
    # Create the plot

    # Plot the both functions
    ax.plot(x, y1, 'g', label=r'$(3\cos{x})^2 + 1$')
    ax.plot(x, y2, 'b', label=r'$2\sin{(x^2)} + 5x - 15$')

    ax.set_title("10.4 Function Plot (pate2499)")   

    # Set x-axis limits and custom ticks
    ax.set_xlim(0, 2 * np.pi + 0.5)
    xticks = [np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    xtick_labels = [r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtick_labels)

    # Set y-axis limits and ticks
    ax.set_ylim(-20, 20)
    ax.set_yticks([-20, -10, 10, 20])

    # Customize spines and legend
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')

    ax.legend(loc='lower right')

    plt.savefig("function_plot_pate2499.pdf") 
    plt.show() 


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
