import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Checks for the first format
    if matches := re.findall(r"^(\d\d?) ([P|A])M to (\d\d?) ([P|A])M$", s):

        # Checks the AM & PM
        if matches[0][1] == 'A':
            begin_hour = int(matches[0][0])
        else:
            begin_hour = int(matches[0][0]) + 12
        if matches[0][3] == "A":
            end_hour = int(matches[0][2])
        else:
            end_hour = int(matches[0][2]) + 12

        # Checks Midnight
        if begin_hour == 12 and matches[0][1] == 'A':
            begin_hour = 0
        elif begin_hour == 24:
            begin_hour = 12
        if end_hour == 12 and matches[0][1] == 'A':
            end_hour = 0
        elif end_hour == 24:
            end_hour = 12
         # If no value errors arise, the 24-hr format is returned
        if 0 <= begin_hour <= 24 and 0 <= end_hour <= 24:
            return f"{begin_hour:02}:00 to {end_hour:02}:00"
    # Checks for the second format
    if matches := re.findall(r"^(\d\d?):(\d\d) ([P|A])M to (\d\d?):(\d\d) ([P|A])M$", s):

        # Checks AM & PM
        if matches[0][2] == 'A':
            begin_hour = int(matches[0][0])
            begin_min = int(matches[0][1])
        else:
            begin_hour = int(matches[0][0]) + 12
            begin_min = int(matches[0][1])
        if matches[0][5] == "A":
            end_hour = int(matches[0][3])
            end_min = int(matches[0][4])
        else:
            end_hour = int(matches[0][3]) + 12
            end_min = int(matches[0][4])

        # Checks Midnight
        if begin_hour == 12 and matches[0][2] == 'A':
            begin_hour = 0
        elif begin_hour == 24:
            begin_hour = 12
        if end_hour == 12 and matches[0][2] == 'A':
            end_hour = 0
        elif end_hour == 24:
            end_hour = 12

        # If no value errors arise, return the 24-hr format
        if 0 <= begin_hour <= 24 and 0 <= end_hour <= 24 and 0 <= begin_min <= 59 and 0 <= end_min <= 59:
            return f"{begin_hour:02}:{begin_min:02} to {end_hour:02}:{end_min:02}"

    # Raises a value error if no value is returned until this line
    raise ValueError

if __name__ == "__main__":
    main()