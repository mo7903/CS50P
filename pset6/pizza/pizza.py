from tabulate import tabulate
import sys, csv

# Checks there is 2 command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    # Checks it's a valid CSV file and reads it
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            file = open(sys.argv[1])
            reader = csv.reader(file)
        except FileNotFoundError:
            sys.exit("File does not exist")

# Places the csv reader into a table
table = []
for r in reader:
    table.append(r)

# Using tabulate, the ASCII Art is drawn
print(tabulate(table[1:], table[0], tablefmt="grid"))