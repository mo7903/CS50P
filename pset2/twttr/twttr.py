# Prompts user for inpur
long = input("Input: ")
shrt = ""

# Checks for the case where a letter is a vowel
for c in long:
    match c.lower():

        # if so, remove it
        case "a" | "i" | "o" | "u" | "e":
            shrt += ""
        #if not, output it
        case _:
            shrt += c
print(f"Output: {shrt}")