import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Begins counting
    ums = 0

    # Checks string beginning
    if s.lower().startswith("um"):
        ums += 1

    # Counts all matches in string
    if matches := re.findall(r"\sum\W", s, re.IGNORECASE):
        ums += len(matches)

    # Return the number of counts
    return ums



if __name__ == "__main__":
    main()