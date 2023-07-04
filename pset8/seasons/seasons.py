from datetime import date
import sys, inflect

# creates an inflect engine called p
p = inflect.engine()

def main():
    # Inputs user for date of birth
    birth = get_birth(input("Date of Birth: "))

    # Calculates elapsed time till today
    time =  date.today() - birth
    mins = time.days * 24 * 60

    # Uses inflect to turn numbers into letters & prints them
    letters = p.number_to_words(mins, andword="")
    print(letters[0].capitalize() + letters[1:], "minutes")

# Takes the string input, splits it, and checks it, exitting if an error happens
def get_birth(birth):
    s = birth.split("-")
    try:
        return date(int(s[0]), int(s[1]), int(s[2]))
    except (ValueError, IndexError):
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()