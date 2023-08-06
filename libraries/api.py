import requests
from sys import argv, exit

if len(argv) == 2:
    try:
        n = float(argv[1])
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
            price = response['bpi']['USD']['rate_float']
        except requests.RequestException:
            exit("cannot complete API request")
    except:
        exit("cannot convert argument to float")
else:
    exit("Invalid arguments")
print(f"${n*price:,.4f}")