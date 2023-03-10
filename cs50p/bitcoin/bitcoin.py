import requests
import sys

try:
    bitcoins = sys.argv[1]
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    value = response["bpi"]["USD"]["rate"]
    value = value.replace(",", "")
    amount = float(value) * float(bitcoins)
    print(f"${amount:,.4f}")
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")