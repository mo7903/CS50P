import requests, sys

# Checks that the user entered a command-line argument
if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

# Gets the rate from API request and multiplies it by entered factor
try:
    rate = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()["bpi"]["USD"]["rate_float"]
    amount = rate*float(sys.argv[1])

# If the user did not cooperate, the system exits
except (requests.RequestException, ValueError):
    sys.exit("Command-line is not a number")

# If no problems arise, print the amount in USD
else:
    print(f"${amount:,.4f}")