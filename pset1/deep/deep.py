# Inputs user for answer
ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# removes whitespace and lowercases everything
match ans.strip().lower():

    # checks for 42
    case "42" | "forty-two" | "forty two":
        print("Yes")

    # otherwise print no
    case _:
        print("No")