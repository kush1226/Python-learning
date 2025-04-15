"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 11.4 - bank accounts
Date: 04/13/2025

Description:
    This Python program defines Account and Savings classes to manage deposits, withdrawals, and interest. It prints account activity and handles insufficient funds, simulating basic bank operations with clear output formatting.
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

class Account:
    def __init__(self, balance): # Initialize the account with a starting balance
        self.balance = balance
        print(f"New account balance: ${self.balance:.2f}")

    def deposit(self, amount):
        print(f"Deposit: ${amount:.2f}")  # Method to deposit money into the account
        self.balance += amount

    def withdraw(self, amount):
        print(f"Withdraw: ${amount:.2f}") # Method to withdraw money from the account
        if amount > self.balance:
            print("Insufficient funds. Withdrawal canceled.")
        else:
            self.balance -= amount

    def get_balance(self):
        print(f"Balance: ${self.balance:.2f}")

class Savings(Account):
    def __init__(self, balance, interest_rate): # Initialize with a balance and interest rate
        super().__init__(balance)
        self.interest_rate = interest_rate

    def accrue_interest(self):
        interest = self.balance * self.interest_rate  # Method to apply interest to the balance
        print(f"Interest payment: ${interest:.2f}")
        self.balance += interest

def main(): #add the initial balance and interest rate and make transactions 
    account = Savings(200.00, 0.10) 
    account.get_balance()
    account.deposit(12.34)
    account.get_balance()
    account.withdraw(40.00)
    account.get_balance()
    account.withdraw(200.00)
    account.get_balance()
    account.accrue_interest()
    account.accrue_interest()
    account.accrue_interest()
    account.withdraw(200.00)
    account.get_balance()

if __name__ == "__main__":
    main()
