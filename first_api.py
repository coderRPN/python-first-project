import requests
import json

import watchdog

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)


parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "BTCGBP",
    "apikey": "FMYE8JOCVC65C1JM"
}

response = requests.get("https://www.alphavantage.co/query", params=parameters)
jprint(response.json())

print("----------------------")

meta_data = response.json()['Meta Data']
jprint(meta_data)
