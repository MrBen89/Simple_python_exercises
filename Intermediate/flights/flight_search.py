import requests
from datetime import datetime, timedelta
SHEETY_API = "https://api.sheety.co/e25c3800336773ce148c134eef069c3b/flightDeals/prices"
SEARCH_API = "https://api.tequila.kiwi.com/v2"
API_KEY = "key"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_iata(self, name):
        print(f"testing {name}")
        return(f"testing {name}")

    def price_search(self, code):
        now = datetime.now()
        six_months = (datetime.now() + timedelta(days = 180))
        headers = {
            "apikey": API_KEY,
        }
        body = {
            "fly_from": "LON",
            "fly_to": code,
            "date_from": now.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=f"{SEARCH_API}/search", headers=headers, params=body)
        print(code, response.json()["data"][0]["price"])
