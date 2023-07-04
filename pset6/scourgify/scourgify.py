import sys, csv

# Checks there is 3 command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    # Checks that both are valid CSV files
    if not sys.argv[1].endswith("csv"):
        sys.exit("Could not read" + sys.argv[1])
    else:
        try:
            before = open(sys.argv[1])
            reader = csv.DictReader(before)
        except FileNotFoundError:
            sys.exit("Could not read" + sys.argv[1])

# Goes through the original file to get name and house while modifying name
table = []
for row in reader:
    last, first = row["name"].split(", ")
    table.append({"first": first, "last": last, "house": row["house"]})

# Opens file2 in write mode to write the new fields
with open(sys.argv[2], "w") as after:
    writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for line in table:
        writer.writerow(line)