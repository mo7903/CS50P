# Defines the cost at first as 50
due = 50

# Prompts user for coins until the due is paid
while due > 0:
    print(f"Amount Due: {due}")
    money = int(input("Insert Coin: "))
    if money in [5, 10, 25]:
        due -= money

# Prints the change owed to user
print(f"Change Owed: {0 - due}")