"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 10.1 - monthly sales
Date: 03/30/2025

Description:
    This Python program collects monthly sales data from the user, stores it in a list, and generates a pie chart using Purdue's retired secondary color palette, with month labels and a title including the Purdue login.
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

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    sales = []
    
    for month in months:
        value = float(input(f"Enter the sales for {month[:3]}: ")) # Ask user for sales value for each month
        sales.append(value)
    
    purdue_colors = [
    "#5B6870",  # EverTrueBlue
    "#6E99B4",  # SlayterSkyBlue
    "#A3D6D7",  # AmeliaSkyBlue
    "#085C11",  # LandGrantGreen
    "#849E2A",  # RossAdeGreen
    "#C3BE0B",  # CeleryBogGreen
    "#E9E45B",  # SpringFestGreen
    "#6B4536",  # OakenBucketBrown
    "#B46012",  # BellTowerBrick
    "#FF9B1A",  # MackeyOrange
    "#FFD100",  # YellowWalk
    "#29A592"   # FountainRunTeal
    ]
    
    plt.pie(sales, colors=purdue_colors, labels=months) # Initiate pie char for the data given by user
    plt.title("Monthly Sales for pate2499")                  
    plt.savefig("monthly_sales_pate2499.pdf")                
    plt.show()                                             


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
