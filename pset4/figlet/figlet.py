# Imports the needed fonts and functions from outside modules
import sys, random
from pyfiglet import Figlet
figlet = Figlet()
fonts = figlet.getFonts()

# Tries to select a font from command-line
try:

    # Looks in the library of fonts for the desired one
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet.setFont(font=sys.argv[2])
        else:
            raise Exception("a7a")

    # Randomizes the font if none is provided
    elif len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts))

    # Exits if the command-line args are not 0 or 2
    else:
        raise Exception("a7a")

# Any exceptions raised exit the program signaling invalid usage
except (IndexError, Exception):
    sys.exit("Invalid Usage")

# If all is okay, the program takes input from the user to format in the desired font
else:
    s = input("Input: ")
    print(figlet.renderText(s))