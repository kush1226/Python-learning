"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 08.6 - Step Counter
Date: 03/21/2025

Description:
    This program reads steps.txt, calculates the average daily steps for each month in a non-leap year, and displays results with set decimal precision, ensuring output format matches the provided sample exactly.
    
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
    # List of tuples containing month names and their respective number of days
    months = [
        ("January", 31), ("February", 28), ("March", 31),
        ("April", 30), ("May", 31), ("June", 30),
        ("July", 31), ("August", 31), ("September", 30),
        ("October", 31), ("November", 30), ("December", 31)
    ]
    
    steps = [] 
    with open("steps.txt", "r") as file:
        for line in file:  # Read each line from the file
            number = int(line.strip())  # Convert the line to an integer
            steps.append(number)  # Add the integer to the steps list
    
    index = 0  # Initialize index for slicing step data
    print("The average steps taken each month were:")

    for month, days in months:  
        month_steps = steps[index:index+days]  # Extract step data for the current month
        avg = sum(month_steps) / days  # Calculate the average step count for the month
        index += days  # Update index to point to the next month's data
        print(f"{month:>10} : {avg:8.2f}")  


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
