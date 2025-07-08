import requests
import sys
import json

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    resp = r.json()
    rate = float((resp["bpi"]["USD"]["rate"]).replace(',',''))
    print(f"${(float(sys.argv[1])*rate):,.4f}")

except requests.RequestException:
    sys.exit()