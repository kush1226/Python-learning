"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 08.1 - pig latin
Date: 03/11/2025

Description:
    This program converts a given sentence from Pig Latin to English. It moves the third-to-last letter of each word to the front and removes the "ay" suffix, then outputs the translated English sentence.
    
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
def pig(s):
    word_list = s.split() # to split the word                
    translated = []                                    
    for word in word_list:
        translated_word = word[-3] + word[:-3] # we put -3th first and continue till -4 to the end
        translated.append(translated_word)

    final = ' '.join(translated)                       
    final = final.lower() #to make all the letters in lower case                        
    final = final.capitalize() #to make the first letter capital                          
    
    return final

def main():

    input_string = (input("Enter a string in Pig Latin: ")) #input
    translated = pig(input_string)                              
    print("Translation:", translated)                          



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

