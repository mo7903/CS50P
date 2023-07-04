def main():
    while True:
        # Prompts user for a fraction constantly until one is given
        frac = input("Fraction: ")

        # Tries to process the fraction given by user
        try:
            fuel = convert(frac)
        # Any exception of those reruns the loop
        except (ValueError, ZeroDivisionError, IndexError):
            continue
        else:
            print(f"{gauge(fuel)}")
            break



def convert(fraction):
    nums = fraction.split("/")
    num = int(nums[0])
    den = int(nums[1])
    frac = num/den

   # Raises an exception if the number is more than 1
    if frac > 100:
        raise ValueError
    else:
        frac = frac * 100
        return int(frac)


def gauge(percentage):
    # If no exceptions arise, gauge the percentage
    if 100 >= percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()