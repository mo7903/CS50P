# List with all months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
lis = []
ls = []

# Continue to prompt the user until a valid date is given
while True:
    try:
        date = input("Date: ")

        # If the date is in the format of MM/DD/YYYY
        lis = date.split('/')
        if len(lis) == 3:
            if 0 < int(lis[0]) < 13:
                month = int(lis[0])
            if 0 < int(lis[1]) < 32:
                day = int(lis[1])
            if 10000 > int(lis[-1]) > 999:
                year = int(lis[-1])

        # If the date is in the format of Month DD, YYYY
        elif len(date.split(',')) == 2:
            ls = date.split()
            month = months.index(ls[0]) + 1
            if 0 < int(ls[1].rstrip(',')) < 32:
                day = int(ls[1].rstrip(','))
            if 10000 > int(ls[-1]) > 999:
                year = int(ls[-1])
        print(f"{year}-{month:02}-{day:02}")

    # If any error arises, reprompt the user with the while loop
    except (ValueError, NameError, IndexError):
        continue

    # If no errors arise, break out of the loop
    else:
        break

