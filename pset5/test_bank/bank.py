def main():
    # prompts user for greeting
    greet = (input("Greeting: "))
    print(f"${value(greet)}")

def value(greeting):
    greeting = greeting.lower().strip()
    # does the greeting start with an h?
    if greeting[0] == "h":

        # did he say "hello" explicitly?
        if "hello" in greeting:
            return 0

        # alright you got a greeting that starts with an h
        else:
            return 20

    else:
        return 100


if __name__ == "__main__":
    main()