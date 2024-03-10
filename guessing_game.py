"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Imports the random module.

import random


# The main game function.

def start_game():

# Displays welcome message

    print("-" * 40)
    print("  Welcome to the Number Guessing Game!")
    print("-" * 40)

#   Gets random number

    answer = random.randint(1,10)
    number_of_guesses = 0
    high_score = 0
    number_of_plays = 0
    
# Starts loop for guesses

    while True:

# Asks for guess
        
        try:
            guess = int(input("\nPick a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                raise ValueError
            number_of_guesses  += 1
            
# If guess is lower

            if guess > answer:
                print("It's lower") 

            
# If guess is higher

            elif guess < answer:
                print("It's higher")
            
# If guess is correct

            else:
                print("Got it!")

# Shows number of attempts

                if number_of_guesses == 1:
                    tries = "try"
                else:
                    tries = "tries"
                print("It took you", number_of_guesses, tries, ".")

# Would the player like to play again?
# Yes, set high score? game is reset, new random number, new game
# No, Goodbye message and game ends

                number_of_plays += 1
                play_again = input("Would you like to play again? y/n ")



                if play_again.lower() == "y":
                    if number_of_plays == 1:
                        high_score = number_of_guesses
                    else:
                        if number_of_guesses < high_score:
                            high_score = number_of_guesses



                    print("Great!  The High Score is", high_score)
                    answer = random.randint(1,10)
                    number_of_guesses = 0
                else:
                    print("The game is now over.  See you next time!")
                    break

# Exception handling

        except ValueError:
            print("\nI'm sorry, the number needs to be a whole number between 1 and 10.\n")


# Starts the game!

start_game()
