#!/usr/bin/env python3
"""
Created by: Xiaohan Tian
Created on: Mar 18, 2025
This module holds constants
"""

import constants


def main():
    # get input from users
    guess_number = int(input("Enter the number of your guess between 1 to 9: "))
    print("")

    # if statement and compare with the correct number.
    if guess_number != constants.CORRECT_NUMBER:
        print("You guessed wrong!")

    if guess_number == constants.CORRECT_NUMBER:
        print("You guessed correct!")

    # display the finishing sentence.
    print("\nDone.")


if __name__ == "__main__":
    main()
