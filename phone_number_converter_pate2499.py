"""
Author: Kush Patel, pate2499n@purdue.edu
Assignment: 08.2 - phone number converter
Date: 03/11/2025

Description:
    This program converts phone numbers with letters into numeric format using a standard keypad mapping. It takes user input, replaces letters with digits, and displays both the original and converted number.
    
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
def convert_number(phone):

    letter_to_number = {}
    letter_groups = [  # for mapping the alphabet groups to their respective numbers
        ('ABC', '2'),
        ('DEF', '3'),
        ('GHI', '4'),
        ('JKL', '5'),
        ('MNO', '6'),
        ('PQRS', '7'),
        ('TUV', '8'),
        ('WXYZ', '9'),
    ]

    for letters, num in letter_groups:
        for letter in letters:
            letter_to_number[letter] = num

    converted = []
    for c in phone:
        if c.isalpha():
            converted.append(letter_to_number[c.upper()])  # Convert letters
        else:
            converted.append(c)                            
    return ''.join(converted)


def main():
    phone = input("Enter a telephone number: ") # input by user
    converted = convert_number(phone)  
    print(f"  {phone}") # Print orignal 
    print(f"  {converted}") # Print converted


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()