total = 0
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
while True:
    try:
        # Prompts user for item and looks up the dict for it
        total += menu[input("Item: ").title()]

    # A Key error re-prompts the user
    except KeyError:
        continue

    # Pressing Ctrl-d breaks the loop and the ends the order
    except EOFError:
        print()
        break

    # If no error occurs, the total is shown and the user can order again
    else:
        print(f"Total: ${total:.2f}")