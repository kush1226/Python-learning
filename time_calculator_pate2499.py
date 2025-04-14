"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 02.4 -  time calculator
Date: 02/01/2025

Description:
    The program is to build a time calculator which determines days, hours and minutes based on the seconds that are input.
Contributors:
    Name, login@purdue.edu [repeat for each]

My contributors helped me:
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
    """
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 02.4 -  Time Calculator
Date: 02/01/2025

Description:
    The program is to build a time calculator which determines days, hours, and minutes based on the seconds that are input.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributors helped me:
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
    another student access to my code. The project I am
    submitting is my own original work.
"""

def main():
    time = int(input("Please enter a time in seconds: "))
    seconds = time
 
    # Define time units in seconds
    minute = 60
    hour = minute * 60
    day = hour * 24
 
    # Calculate days, hours, minutes, and seconds
    days = seconds // day
    seconds %= day
    hours = seconds // hour
    seconds %= hour
    minutes = seconds // minute
    seconds %= minute
 
    # Format and display the result
    if time< 60:
        print(f'  {time} seconds is less than one minute.')
    else:
        print(f"  {time:,} seconds equals ", end='')
        if days:
            print(f"{days:,} day(s)", end='')
            if hours or minutes or seconds:
                if hours and (minutes or seconds):
                    print(", ", end='')
                elif minutes and seconds:
                    print(", ", end='')
                else:
                    print(" and ", end='')
 
        if hours:
            print(f"{hours} hour(s)", end='')
            if minutes and seconds:
                print(", ", end='')
            elif minutes or seconds:
                print(" and ", end='')
 
        if minutes:
            print(f"{minutes} minute(s)", end='')
            if seconds:
                print(" and ", end='')
 
        if seconds:
            print(f"{seconds} second(s)", end='')
 
        print(".")
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
