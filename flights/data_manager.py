import requests
SHEETY_API = "https://api.sheety.co/e25c3800336773ce148c134eef069c3b/flightDeals/prices"
TEQUILA_API = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_API_KEY = "secret"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def populate_data(self):
        response = requests.get(url=SHEETY_API)
    #for num in range (0, len(response.json()["prices"])):
        #print(response.json()["prices"][num]["city"])
        return(response.json())

    def update_code(self, id, city):
        headers = {
            "apikey": TEQUILA_API_KEY,
        }
        body = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(url=TEQUILA_API, headers=headers, params=body)
        code = response.json()["locations"][0]["code"]


        body = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(url=f"{SHEETY_API}/{id}", json=body)
        print(response.json())
