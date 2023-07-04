# Prompts user for camelCase input
cc = input("camelCase: ")

# Defines an empty string for snake
snake = ""

# Iterates over each char in the input string
for c in cc:

    # if it's upper, then make it lower preceded by an underscore
    if c.isupper():
        snake += "_" + c.lower()
    else:
        snake += c
print(snake)