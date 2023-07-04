# Imports inflect package
import inflect
p = inflect.engine()

# Prepares an empty list for the names
names = []

# Keeps prompting the user for more names until Ctrl-D
while True:
    try:
        # Adds any new name to the list of names
        names.append(input("Name: "))

    # At hitting Ctrl-D
    except EOFError:

        # bye is made with join from inflect to write the adieu and break the while loop
        bye = p.join(names)
        print("Adieu, adieu, to", bye)
        break