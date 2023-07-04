import re

def main():
    print(validate(input("IPv4 Address: ")))

# Goes through the ip address and matches it with the format and returns a boolean
def validate(ip):
    if re.fullmatch(r"(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()