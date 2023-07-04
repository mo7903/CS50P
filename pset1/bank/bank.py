# prompts user for greeting
greet = (input("Greeting: ")).lower().strip()

# does the greeting start with an h?
if greet[0] == "h":

    # did he say "hello" explicitly?
    if "hello" in greet:
        print("$0")

    # alright you got a greeting that starts with an h
    else:
        print("$20")

else:
    print("$100")