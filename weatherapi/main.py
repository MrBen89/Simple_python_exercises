import requests
import math
import os

rate_list = []

url = "https://api.apilayer.com/fixer/convert?to=JPY&from=GBP&amount=7500"

api_key = os.environ.get("APILAYER_API_KEY")
payload = {}
headers= {
  "apikey": api_key
}

response = requests.request("GET", url, headers=headers, data = payload)
print(response)
conversion_data = response.json()
print(math.floor(conversion_data["result"]))
print(conversion_data["date"])

rate_list.append({"date":conversion_data["date"], "cost":conversion_data["result"]})

print(rate_list)
file = open("rate_list.txt", "a")
file.write(f"{rate_list}\n")
file.close()
