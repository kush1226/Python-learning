"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 09.2 - world series
Date: 03/30/2025

Description:
    In this program, the user enters a year to find out which team won the World Series that year. The program then displays the winning team's name along with the total number of times the team has won the World Series.
    
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

def load_winners_data():

    team_wins = {}
    year_winners = {}

    start_year = 1903 # first year in the file where world series are played
    skipped_years = {1904, 1994} # World Series wasn't played in these years

    lines = []
    with open("WorldSeriesWinners.txt", "r") as file:
        for line in file:
            lines.append(line.strip())  # Removes newlines and spaces
    
    # print(lines)
    year = start_year

    for team in lines:
        while year in skipped_years: # Skip years where the World Series wasn't played
            year += 1 # Move to the next year if current year is invalid

        year_winners[year] = team
        team_wins[team] = team_wins.get(team, 0) + 1 # This increments the number of times the team has won by 1.
        year += 1  # Move to the next valid year

    return team_wins, year_winners


def main():

    team_wins, year_winners = load_winners_data()

    year = int(input("Enter a year in the range 1903 -- 2023: "))
    
    if year < 1903 or year > 2023:
        print(f"  Data for the year {year} is not included in this system.")
    elif year in {1904, 1994}:
        print(f"  The World Series wasn't played in the year {year}.")
    else:
        team = year_winners[year]
        wins = team_wins[team]
        print(f"  The {team} won the World Series in {year}.")
        print(f"  They have won the World Series {wins} times.")

        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
