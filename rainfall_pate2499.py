"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 03.3 -  rainfall
Date: 02/09/2025

Description:
    The program is to collect data and calculate the average rainfall over a period of years. 
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
    months_in_year = 12
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] #all 12 months are here to print one after other

    years = int(input("Enter the number of years: "))
    
    if years <= 0:
        print("Invalid input; years must be greater than 0.")#years should be always positive and also not zero
        return

    total_rainfall = 0.0
    total_months = years * months_in_year

    for year in range(1, years + 1):
        print(f"  For year No. {year}")
        
        for month in month_names:
            while True:
                rainfall = float(input(f"    Enter the rainfall for {month}.: "))
                if rainfall < 0:
                    print("    Invalid input; rainfall cannot be negative.")
                else:
                    total_rainfall += rainfall
                    break

    print(f"There are {total_months} months.")
    print(f"The total rainfall was {total_rainfall:.2f} inches.")
    print(f"The monthly average rainfall was {total_rainfall / total_months:.2f} inches.")

if __name__ == "__main__":
    main()

