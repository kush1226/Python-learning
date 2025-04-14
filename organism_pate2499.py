"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 03.4 -  organism
Date: 02/09/2025

Description:
    The program is to predicts the approximate size of a population of organisms.
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
    #  input
    start = float(input("Starting population, in thousands: "))
    increase_percent = float(input("Average daily increase, in percent: "))
    days = int(input("Number of days to multiply: "))

    # Convert percentage to decimal
    rate = increase_percent / 100

    # Print header
    print("Day   Approx. Pop")

    # Initialize population and display day 0
    population = start
    print(f"  0    {population:10,.3f}")

    # Calculate and display population for each day
    for day in range(1, days + 1):
        population += population * rate
        print(f"{day:3}    {population:10,.3f}")

if __name__ == "__main__":
    main()

