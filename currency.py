import requests

API_KEY = "fca_live_eLHOBqcIWUixS8eSRpHJE7rUgxavn1iCmnFndBrV"

BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"


CURRENCIES =["USD","CAD","INR","EUR","AUD","CNY"]

def convert_Currency(base):
    currenices = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currenices}"
    try:
        response = requests.get(url)
        data = response.json()
        # print(data)
        return data['data']
    except Exception as e:
        print("Invalid request")
        return None

while True:
    base = input("Enter the base currency or (q for exit): ").upper()
    if base == 'Q':
        break
    
    
    data = convert_Currency(base)
    if not data:
        continue
    
    del data[base]
    # print(data)
    for ticker,value in data.items():
        print(f"{ticker}:{value}")