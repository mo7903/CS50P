# Prompts user for dollars and percent to calculate tip
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Transforms dollar string to float
def dollars_to_float(d):
    return float(d.lstrip("$"))

# Transforms percentage as a float
def percent_to_float(p):
    return float(p.rstrip("%")) / 100


main()