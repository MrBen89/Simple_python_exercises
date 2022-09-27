import requests
from datetime import datetime

USERNAME = "brp21"
TOKEN = "Jalapeno"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "Jalapeno",
    "username": "brp21",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#

graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "18.5",
}


pixel_post_endpoint = f"{graph_endpoint}/{GRAPHID}"
response = requests.post(url=pixel_post_endpoint, json=pixel_params, headers=headers)

print(response.text)
