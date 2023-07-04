def main():
    # Prompts user for time and converts it to a float
    time = convert(input("What time is it? "))

    # Checks what meal is it according to the time of day
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


# converts time from the 24-hour format
def convert(time):
    times = time.split(":")
    hour = float(times[0])
    minu = float(times[1])
    return hour + minu/60



# Checks that meal.py is called directly
if __name__ == "__main__":
    main()