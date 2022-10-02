from flask import Flask, render_template
import requests



app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/b3a3863991f5dd01b761")
    all_posts = response.json()
    print(all_posts)
    return render_template("index.html", posts=all_posts)

@app.route("/blog/<id>")
def get_blog(id):
    response = requests.get("https://api.npoint.io/b3a3863991f5dd01b761")
    post = response.json()[int(id)]
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
