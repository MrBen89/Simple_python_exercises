from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess/<name>")
def person(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    gender = response.json()["gender"]
    response = requests.get(f"https://api.agify.io?name={name}")
    age = response.json()["age"]
    return render_template("index.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)
