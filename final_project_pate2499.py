"""
Author: Kush Patel, pate2499@purdue.edu
Assignment: 12.1 - Code Breakers - Final Project
Date: 04/27/2025

Description:
    This Python game simulates a password guessing challenge where players guess a 4-digit password. It includes saving/loading game states, showing feedback, and providing an interactive menu for game actions.

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


import random
import json
import os
import datetime
import re

SAVE_FILE = 'saves.json'
MIN_LEN = 4
MAX_LEN = 6
MAX_GUESSES = 10


"""Write new functions below this line (starting with unit 4)."""

def generate_solution(min_length, max_length):
    length = random.randint(min_length, max_length)
    return ''.join(str(random.randint(0, 5)) for _ in range(length))

def load_saves():
    if not os.path.exists(SAVE_FILE):
        return [None, None, None]
    try:
        with open(SAVE_FILE, 'r') as f:
            data = json.load(f)
            if isinstance(data, list) and len(data) == 3:
                return data
    except Exception:
        pass
    return [None, None, None]

def save_saves(slots):
    with open(SAVE_FILE, 'w') as f:
        json.dump(slots, f)

def print_intro():
    print(" You were on your way home to Purdue when you received a text from your")
    print("friend, Timmy. They seemed to have forgotten their favorite COMP 15200-C")
    print("textbook in CBOB building. However, CBOB has recently added a new feature")
    print("to thier doors... A PASWORD LOCK!  OH NO! There's more... IU is trying to")
    print("steal the sacred COMP 15200-C textbook. You need to guess the password")
    print("before they find the textbook and return it Timmy!")
    print()
    print("Will you be able to break this lock before the sacred text is lost forever?")
    print()

def print_menu():
    print("Menu:")
    print("--------------------------------------------------------------------------")
    print("   1: Rules")
    print("   2: New Game")
    print("   3: Load Game")
    print("   4: Quit")

def show_rules():
    print()
    print("Rules:")
    print("--------------------------------------------------------------------------")
    print("1. You get 10 guesses to break the lock.")
    print()
    print("2. Guess the correct code to win the game.")
    print()
    print("3. Codes can be either 4, 5, or 6 digits in length.")
    print()
    print("4. Codes can only contain digits 0, 1, 2, 3, 4, and 5.")
    print()
    print("5. Clues for each guess are given by a number of red and white pins.")
    print()
    print("   5-a. The number of red pins in the R column indicates the number of digits")
    print("      in the correct location.")
    print("   5-b. The number of white pins in the W column indicates the number of")
    print("      digits in the code, but in the wrong location.")
    print("   5-c. Each digit of the solution code or guess is only counted once in the")
    print("      red or white pins.")

def print_board(state, reveal=False):
    sol = state['solution']
    guesses = state['guesses']
    border = "  =+=================+====+="
    print(border)
    if reveal:
        row = list(sol) + ['o'] * (6 - len(sol))
    else:
        row = ['o'] * 6
    print("    " + "  ".join(row) + " | R W  ")
    print(border)
    for i in range(MAX_GUESSES - 1, -1, -1):
        if i < len(guesses):
            g = guesses[i]['guess']
            r = guesses[i]['r']
            w = guesses[i]['w']
            row = list(g) + ['o'] * (6 - len(g))
            print("    " + "  ".join(row) + f" | {r} {w}  ")
        else:
            print("    o  o  o  o  o  o | 0 0  ")
    print(border)

def save_game(state):
    slots = load_saves()
    print()
    print("Files:")
    print("--------------------------------------------------------------------------")
    for idx, slot in enumerate(slots, start=1):
        if slot is None:
            print(f"   {idx}: empty")
        else:
            print(f"   {idx}: {slot['name']} - Time: {slot['time']}")
    while True:
        choice = input("What save would you like to overwrite (1, 2, 3, or c to cancel): ").strip()
        if choice == 'c':
            print("cancelled")
            return False
        if choice in ('1','2','3'):
            si = int(choice) - 1
            break
        print("Please pick a valid save file.")
    while True:
        name = input("What is your name (no special characters): ").strip()
        if re.fullmatch(r"[A-Za-z0-9 ]+", name):
            break
        print("That is an invalid name.")
    slots[si] = {
        'name': name,
        'time': datetime.datetime.now().isoformat(timespec='seconds'),
        'state': state
    }
    save_saves(slots)
    print(f"Game saved in slot {si+1} as {name}.")
    return True

def load_game_slot():
    slots = load_saves()
    print()
    print("Files:")
    print("--------------------------------------------------------------------------")
    for idx, slot in enumerate(slots, start=1):
        if slot is None:
            print(f"   {idx}: empty")
        else:
            print(f"   {idx}: {slot['name']} - Time: {slot['time']}")
    while True:
        choice = input("What save would you like to load (1, 2, 3, or c to cancel): ").strip()
        if choice == 'c':
            print("cancelled")
            return None
        if choice in ('1','2','3'):
            si = int(choice) - 1
            if slots[si] is None:
                print("That file is empty!")
                continue
            return slots[si]['state']
        print("Please pick a valid save file.")

def play_game(initial_state=None, header="New Game:"):
    if initial_state is None:
        state = {
            'solution': generate_solution(MIN_LEN, MAX_LEN),
            'guesses': []
        }
    else:
        state = initial_state

    print()
    print(header)
    print("--------------------------------------------------------------------------")
    print_board(state, reveal=False)

    while True:
        g = input("What is your guess (q to quit, s to save and quit): ").strip()
        if g.lower() == 'q':
            print("Ending Game.")
            return
        if g.lower() == 's':
            if save_game(state):
                print("Ending Game.")
                return
            else:
                # Reprint the board after canceling save
                print_board(state, reveal=False)
                continue

        # Validation
        if len(g) < MIN_LEN:
            print(f'Your guess was "{g}". Invalid guess type! Your guess is too short.')
            print(f"Guess lengths must be between {MIN_LEN} and {MAX_LEN}.")
            continue
        if len(g) > MAX_LEN:
            print(f'Your guess was "{g}". Invalid guess type!')
            print(f"Guess lengths must be between {MIN_LEN} and {MAX_LEN}.")
            continue
        if not g.isdigit():
            print(f'Your guess was "{g}". Invalid guess type! The guess must be only numbers!')
            continue
        if any(c not in '012345' for c in g):
            print(f'Your guess was "{g}". Invalid guess type! The guess must be only numbers 0 through 5.')
            continue

        # Compute pins
        sol = state['solution']
        red = sum(1 for i, ch in enumerate(g) if i < len(sol) and sol[i] == ch)
        sol_counts = {}
        guess_counts = {}
        for i, ch in enumerate(g):
            if i < len(sol) and sol[i] == ch:
                continue
            if i < len(sol):
                sol_counts[sol[i]] = sol_counts.get(sol[i], 0) + 1
            guess_counts[ch] = guess_counts.get(ch, 0) + 1
        white = sum(min(guess_counts.get(d, 0), sol_counts.get(d, 0)) for d in guess_counts)

        state['guesses'].append({'guess': g, 'r': red, 'w': white})

        # Check for correct guess
        if g == sol:
            print_board(state, reveal=True)
            print("You did it! You got Timmy's book!")
            print("Now Timmy can achieve his dreams of being a CS 15900 TA!")
            print("  ...")
            print("Ending Game.")
            return

        # Check for maximum guesses reached
        if len(state['guesses']) >= MAX_GUESSES:
            print_board(state, reveal=True)
            print("You hear a machine yell OUT OF TRIES!")
            print("  ...")
            print("With your frustration at its limit, you tell Timmy you couldn't do it and IU steals the book.")
            print("  ...")
            print("Ending Game.\n")
            return

        # Show updated board after each guess
        print_board(state, reveal=False)

def main():
    print_intro()
    while True:
        print_menu()
        choice = input("Choice: ").strip()
        if choice == '1':
            show_rules()
        elif choice == '2':
            play_game(initial_state=None, header="New Game:")
        elif choice == '3':
            loaded = load_game_slot()
            if loaded is not None:
                play_game(initial_state=loaded, header="Resume Game:")
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")
        print()

if __name__ == "__main__":
    main()