"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 11.3 - rockets
Date: 04/13/2025

Description:
    This program defines Rocket and ReusableRocket classes to calculate and display the cost per launch using given cost data. It demonstrates inheritance and method overriding with real-world inspired rocket examples.
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
class Rocket: #for rockets which are not reusable 
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost):
        self.name = name
        self.booster_cost = booster_cost
        self.upper_stage_cost = upper_stage_cost
        self.fuel_cost = fuel_cost

    def cost_per_launch(self):
        total_cost = self.booster_cost + self.upper_stage_cost + self.fuel_cost #total cost per launch for non reusable rockets
        print(f"This {self.name} cost ${total_cost:.2f} million per launch.")

class ReusableRocket(Rocket): #for rockets which are reusable 
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost, uses):
        super().__init__(name, booster_cost, upper_stage_cost, fuel_cost)
        self.uses = uses

    def cost_per_launch(self):
        total_cost = (self.booster_cost / self.uses) + self.upper_stage_cost + self.fuel_cost #total cost per launch for reusable rockets
        print(f"This {self.name} cost ${total_cost:.2f} million per launch.")

def main():
    rocket1 = Rocket("Atlas V", 65.4, 42.6, 0.23) #cost variables associated with Atlas V
    rocket2 = Rocket("Ariane 5", 83.5, 55.6, 0.69) #cost variables associated with Ariane 5
    rocket3 = Rocket("Long March 3B", 28.5, 19.0, 2.38) #cost variables associated with Long March 3B
    rocket4 = Rocket("Soyuz 2", 20.9, 13.9, 0.24) #cost variables associated with Soyuz 2
    rocket5 = ReusableRocket("Falcon 9", 43.0, 18.6, 0.45, 23) #cost variables associated with Falcon 9

    rocket1.cost_per_launch()
    rocket2.cost_per_launch()
    rocket3.cost_per_launch()
    rocket4.cost_per_launch()
    rocket5.cost_per_launch()

if __name__ == "__main__":
    main()
