import sys

# Checks there is 2 command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:

    # Checks it's a valid python file
    file_name = sys.argv[1]
    if file_name.endswith(".py") == False:
        sys.exit("Not a Python file")
    else:
        try:
            file = open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File does not exist")

# Reads all lines and checks for comments (#) or whitespace
n = 0
for line in file.readlines():
    if not line.lstrip().startswith("#") and not line.isspace():
        n += 1

print(n)