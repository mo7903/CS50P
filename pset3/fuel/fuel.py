while True:
    # Prompts user for a fraction constantly until one is given
    nums = input("Fraction: ").split("/")

    # Tries to process the fraction given by user
    try:
        num = int(nums[0])
        den = int(nums[1])
        frac = num / den

        # Raises an exception if the number is more than 1
        if frac > 1:
            raise Exception("More than 100%")

    # Any exception of those reruns the loop
    except (ValueError, ZeroDivisionError, Exception):
        continue

    # If no exceptions arise, go through the code normally
    else:
        if 1 >= frac >= 0.99:
            print("F")
        elif frac <= 0.01:
            print("E")
        else:
            print(f"{frac*100:.0f}%")
        break