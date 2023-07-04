items = {}
while True:
    try:
        # Prompts user for item
        item = input().upper()

        # Increases item by 1 if in list
        items[item] += 1

    # Adds item to list if not there
    except KeyError:
        items[item] = 1
    # Pressing Ctrl-d breaks the loop and the prints the final list
    except EOFError:

        # Alphabetically sorts the dict giving a list
        items = sorted(items.items())

        # Prints each item in the list
        for i in range(len(items)):
            print(items[i][1], end=" ")
            print(items[i][0])
        break
