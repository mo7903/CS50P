import sys
from PIL import Image, ImageOps

# Checks there is 3 command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:

    # Checks that both input and output have the same extension
    if sys.argv[1].split(".")[1] != (sys.argv[2].split("."))[1]:
        sys.exit("Input and output have different extensions")
    try:
        # Opens shirt and input photo
        shirt = Image.open("shirt.png")
        photo = Image.open(sys.argv[1])

        # takes the size of the shirt as a tuple
        size = shirt.size

        # Crops the input photo to the appropriate shirt size
        new = ImageOps.fit(photo, size)

        # Pastes the shirt into the cropped input while maintaining the transparent background of the shirt in front
        new.paste(shirt, shirt)

        # Saves the final image into the output
        new.save(sys.argv[2])

    # Exits if any of the files are not found
    except (FileNotFoundError):
        sys.exit("File does not exist")