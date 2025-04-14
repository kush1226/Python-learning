"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 04.2 -  lucky sum
Date: 02/07/2025

Description:
    The program is enter integer values and the function should calculate and return the sum of the lucky numbers.
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

def lucky_sum(num1, num2):
     smaller = min(num1, num2)
     larger = max(num1, num2)
     sum = 0
     for num in range(smaller, larger + 1):
         if num % 7 == 0: #divisiblity by 7 for sum
            sum += num
     return sum 
 
def main():
     num1 = int(input("Enter the first integer: "))#input both the numbers here 
     num2 = int(input("Enter the second integer: "))
     result = lucky_sum(num1, num2)#calculating the lucky sum of both numbers
     print(f"The sum of the lucky numbers is {result:,}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
