"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 09.4 - file analysis
Date: 03/30/2025

Description:
    This program reads two text files, processes words by converting to lowercase and removing punctuation, then creates four files: word frequency for each file, common words, and words unique to one file.
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

import string

"""Write new functions below this line (starting with unit 4)."""
def get_words(filename):
    words = []
    with open(filename, "r") as file:  # Opens the file and returns a list of all the words in it.
        for line in file:
            for word in line.split(): # the line is broken down into words based on whitespace.
                cleaned_word = word.lower().strip(string.punctuation)   # Converting the words to lowercase and remove punctuation from both ends.
                if cleaned_word:  # Skip empty strings
                    words.append(cleaned_word)
    return words

def count_words(word_list):
    word_freq = {}
    for word in word_list:
        word_freq[word] = word_freq.get(word, 0) + 1  # count the appearance of the word and add it to dictionary
    return word_freq

def write_word_frequency(filename, word_freq):
    with open(filename, "w") as file: # Writes the word frequency dictionary to the given file.
        for word in sorted(word_freq.keys()): # The words are written in alphabetical order.
            file.write(f"{word}: {word_freq[word]}\n") 

def write_words_list(filename, words_set):
    with open(filename, "w") as file:
        for word in sorted(words_set):
            file.write(f"{word}\n")
    

def main():
    # Process both input files.
    words1 = get_words("python_1.txt")
    words2 = get_words("python_2.txt")

    # Create word frequency dictionaries.
    freq1 = count_words(words1)
    freq2 = count_words(words2)
    
    # Write the frequency files.
    write_word_frequency("python_1_word_frequency.txt", freq1)
    write_word_frequency("python_2_word_frequency.txt", freq2)
    
    # Create sets of words from each file.
    set1 = set(freq1.keys())
    set2 = set(freq2.keys())
    
    # Find common words and words in either but not both.
    common = set1 & set2
    either_but_not_both = (set1 ^ set2)
    
    # Write the common words and either-but-not-both words to their files.
    write_words_list("common_words.txt", common)
    write_words_list("eitherbutnotboth.txt", either_but_not_both)


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
