"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 10.3 - covid 19 cases
Date: 03/30/2025

Description:
    The program reads Indiana COVID-19 weekly data, computes cumulative cases, and plots them in a bar chart using the week's start date with no gaps between bars.
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
import datetime

"""Write new functions below this line (starting with unit 4)."""


def main():

    week_start_dates = []
    cumulative_cases = []
    total_cases = 0

    # Read the data file and compute the cumulative total cases.
    with open("indiana_covid-19_data_summer_2023.txt", "r") as file:
        for line in file:
            parts = line.split()
            start_date_str = parts[0]   # first column is the week start date.
            new_cases = float(parts[2]) # third column is the new cases for that week.
            total_cases += new_cases

            y, m, d = start_date_str.split('-') # Convert the start date using strip
            dt = datetime.date(int(y), int(m), int(d))
            week_start_dates.append(dt)
            cumulative_cases.append(total_cases/1000)  # make the total case in thousands unit

    fig, ax = plt.subplots()

    plt.bar(week_start_dates, cumulative_cases, width=7)  # bar plot with width 7
    
    # Add labels and title.
    ax.set_xlabel("Date")                                   
    ax.set_ylabel("Number of Cases (in thousands)")       
    ax.set_title("Weekly Positive COVID-19 Cases in Indiana (pate2499)")

    fig.autofmt_xdate() # auto format the date

    plt.savefig("covid_19_cases_pate2499.pdf")
    plt.show()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

