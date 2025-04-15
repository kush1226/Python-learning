"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 11.5 - user privileges
Date: 04/13/2025

Description:
    This program defines two classes: Privileges, which manages user privileges, and User, which stores user details. It demonstrates granting and revoking privileges for a user and displaying the updated user profile after each change.
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

class Privileges:
    def __init__(self, privs={'post', 'interact'}): # Initializes privileges with default values 'post' and 'interact' if none are provided
        self.privs = set(privs)

    def grant(self, priv):
        self.privs.add(priv)   
        print(f"Granted {priv}")

    def revoke(self, priv):
        self.privs.discard(priv)
        print(f"Revoked {priv}")

    def get_privs(self):
        return ', '.join(sorted(self.privs)) # Returns a comma-separated string of privileges in alphabetical order


class User:
    def __init__(self, name, email): # Initializes a user with name, email, and default privileges
        self.name = name
        self.email = email
        self.privs = Privileges()

    def describe_user(self):  
        print("User Profile")
        print(f"  Name: {self.name}")
        print(f"  Email: {self.email}")
        print(f"  Privs: {self.privs.get_privs()}")


def main():
    
    user = User("Alice", "alice@example.com") # Create a user named Alice 
    user.describe_user()

    user.privs.grant("teleport") # Grant 'teleport' privilege
    user.describe_user()

    user.privs.revoke("post") # Revoke 'post' privilege 
    user.describe_user()

if __name__ == "__main__":
    main()
