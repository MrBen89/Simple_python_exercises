import requests
from datetime import datetime
import os

API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]
ENDPOINT =  "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT =  "https://api.sheety.co/e25c3800336773ce148c134eef069c3b/myWorkouts/workouts"

age = 32
weight = 80
query = "cycled for 18 minutes"
today = datetime.now()

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

params = {
    "query": query,
    "weight_kg": weight,
    "height_cm": 175,
    "age": age,
    "gender": "male",
}

response = requests.post(url=ENDPOINT, headers=headers, json=params)
exercise = response.json()["exercises"][0]["user_input"]
duration = response.json()["exercises"][0]["duration_min"]
calories = response.json()["exercises"][0]["nf_calories"]

workout_body = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=workout_body, auth=(os.environ["SHEETYUSER"], os.environ["SHEETYPASS"]))

print(sheety_response.text)
