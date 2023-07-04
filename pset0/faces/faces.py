# Prompts user for string
def main():
    string = input("String: ")
    print(convert(string))

# Converts emoticons to emojis
def convert(this):
    return this.replace(":)", "🙂").replace(":(", "🙁")

main()