# Imports checkers function from library
from validator_collection import checkers

# Prints valid or invalid depending on the output of check
def main():
    if mail_check(input("What's your email address? ")):
        print("Valid")
    else:
        print("Invalid")

# Returns the bool value of checkers email
def mail_check(s):
    return checkers.is_email(s)

if __name__ == "__main__":
    main()