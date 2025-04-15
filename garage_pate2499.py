"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 11.2 - garage
Date: 04/13/2025

Description:
    This program simulates a parking garage system with options to add or remove cars and check availability in two lots. It uses a Garage class with methods to manage car entries, exits, and display the current status.
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
class Garage:
    def __init__(self, name, spaces, cars):
        self.name = name
        self.spaces = spaces
        self.cars = cars

    def car_in(self):
        if self.cars < self.spaces:
            self.cars += 1
            print(f"  Added a car to Lot {self.name}")
        else:
            print(f"  Lot {self.name} is full. Can not add another car.")

    def car_out(self):
        if self.cars > 0:
            self.cars -= 1
            print(f"  Removed a car from Lot {self.name}")
        else:
            print(f"  Lot {self.name} is empty. There are no cars to remove.")

    def status(self):
        available = self.spaces - self.cars
        print(f"  Lot {self.name}: {available} out of {self.spaces} spaces are available.")

def print_menu():
    print("------------ Menu ------------")
    print("  0. Exit")
    print("  1. Print current status.")
    print("  2. Add a car to A lot.")
    print("  3. Add a car to B lot.")
    print("  4. Remove a car from A lot.")
    print("  5. Remove a car from B lot.")

def main():
    # Initialize garages with correct car counts
    lot_a = Garage('A', 10, 8)  # 8 cars initially
    lot_b = Garage('B', 15, 1)  # 1 car initially

    print("Welcome to the Garage Manager!")
    print_menu()  # Print menu once initially

    while True:
        user_input = input("Please choose an option (0-5): ").strip()
        
        # Validate input
        if user_input.isdigit():
            choice = int(user_input)
            if 0 <= choice <= 5:
                if choice == 0:
                    print("End of the Day Garage Status:")
                    lot_a.status()
                    lot_b.status()
                    break
                elif choice == 1:
                    print("Current Garage Status:")
                    lot_a.status()
                    lot_b.status()
                elif choice == 2:
                    lot_a.car_in()
                elif choice == 3:
                    lot_b.car_in()
                elif choice == 4:
                    lot_a.car_out()
                elif choice == 5:
                    lot_b.car_out()
            else:
                print("  Invalid choice!")
                print_menu()  # Reprint menu for out-of-range input
        else:
            print("  Invalid choice!")
            print_menu()  # Reprint menu for non-integer input

if __name__ == "__main__":
    main()
