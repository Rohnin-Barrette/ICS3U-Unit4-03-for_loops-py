#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This program shows the user all of the numbers squared 
# leading up to and including the inputted number 


def main():
    # This program shows the user all of the numbers squared 
    # leading up to and including the inputted number 
    
    # this is to keep track of how many times you go through the loop
    counter = 0
    answer = 0
    
    # input
    user_string = input("please enter a number >= 0: ")
    
    # process and output
    try:
        user_number = int(user_string)
        if user_number >= 0:
            for counter in range(user_number + 1):
                answer = counter * counter
                print("{0}² = {1}".format(counter, answer))
        else:
                print("please enter a positive number.")
    except:
            print("invalid input")
    finally:
            print("\nDone.")
        
        
if __name__ == "__main__":
    main()
        