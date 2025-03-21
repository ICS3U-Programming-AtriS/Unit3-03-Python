#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 21, 2025
# Random Number Guessing Game

import random


def main():
    # Get the user's guess
    user_num = int(input("Enter a number (0-9): "))

    # Generate a random number between 0 and 9 [INCLUSIVE]
    correct_num = random.randint(0, 9)

    # Check if the user's guess is the same as the correct number
    if user_num == correct_num:
        # Tell the user that they guessed correctly
        print("You guessed correctly!")
    # If it isn't, tell the user that they guessed wrong
    else:
        # Tell the user that they guessed wrong
        # Also tell them the correct answer
        print(f"You guessed wrong. The correct answer was {correct_num}")


if __name__ == "__main__":
    main()
