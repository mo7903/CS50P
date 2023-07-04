import random

# Initiates n as 0 to begin the level determination loop
n = 0

while n <= 0:

    # Any case of ValueError reprompts the user for a level
    try:
        lev = int(input("Level: "))

        # Generates a random number between 1 and the level
        n = random.randint(1, lev)

    except ValueError:
        continue


while True:

    # Any case of ValueError reprompts the user for a guess
    try:
        g = int(input("Guess: "))
        
    except ValueError:
        continue

    # If no errors arise, the program checks the guess
    else:
        if g > n:
            print("Too large!")

        elif g < n:
            print("Too small!")

        # If the guess is not larger than or less than the randomly generated number, break out of the guessing loop
        else:
            print("Just right!")
            break