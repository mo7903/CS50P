import random


def main():
    trial = 0
    score = 0
    correct = 1
    level = get_level()
    # Does 10 times for 10 questions
    for _ in range(10):
        trial = 0
        x = generate_integer(level)
        y = generate_integer(level)
        true = x + y

        # Gives 3 trials
        while trial < 3:

            # Prompts user for an answer and checks it
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans != true:
                    correct = 0
                    raise ValueError
            except ValueError:
                print("EEE")
                trial += 1
                continue
            else:
                correct = 1
                score += 1
                break

        # If the user answers incorrectly 3 times, the answer is shown
        if correct == 0:
                print(f"{x} + {y} = {true}")
    # Prints the score / 10 after the 10 questions
    print("Score:", score)

def get_level():
    # Prompts the user for a level until 1, 2, or 3 is submitted
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        else:
            if n in [1, 2, 3]:
                return n
            else:
                continue


def generate_integer(level):
    # Adjusts numbers for the randint function
    if level == 1:
        min = 0
    else:
        min = 10**(level-1)
    max = (10**level) - 1

    # Returns a random integer within the needed range
    return random.randint(min, max)

# Assures the file is not called by another file
if __name__ == "__main__":
    main()
