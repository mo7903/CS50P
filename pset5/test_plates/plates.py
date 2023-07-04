def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Checks for any invalid chars or combinations
def is_valid(s):
    if s.isalnum == False or "." in s:
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    if s.isalpha() == False and s[(s.find("0")) - 1].isalpha():
        return False
    for c in range(len(s) - 1):
        if s[c].isnumeric():
            if s[c + 1].isalpha():
                return False
            else:
                continue
        else:
            continue

    return True

if __name__ == "__main__":
    main()