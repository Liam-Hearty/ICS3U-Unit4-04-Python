#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program makes the user guess the random number.


import random


def main():
    # This program makes the user guess the random number.

    # input, process & output in loop
    try:
        for loop_counter in range(3):
            # Input
            chosen_number = int(input("Enter your guess between 0-9: "))
            # Process
            loop_counter = loop_counter + 1
            random_number = random.randint(0, 9+1)
            if chosen_number == random_number:
                break
            else:
                # Output
                print("Wrong! the number was: {0}".format(random_number))
                print("Lets play again.\n")
        if chosen_number == random_number:  # Winner
            print("\nCongrats! You got it.")
        if chosen_number != random_number:  # Loser
            print("\nMaybe try again next time.")
    except(ValueError):
        print("Please input a positive whole number.")


if __name__ == "__main__":
    main()
