def main():
    # Prompts user for input
    long = input("Input: ")
    print(f"Output: {shorten(long)}")


def shorten(word):
    shrt = ""
    # Checks for the case where a letter is a vowel
    for c in word:
        match c.lower():
            # if so, remove it
            case "a" | "i" | "o" | "u" | "e":
                shrt += ""
            #if not, output it
            case _:
                shrt += c
    return shrt


if __name__ == "__main__":
    main()





