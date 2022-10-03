from flask import Flask, render_template
import requests



app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    print(all_posts)
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"

@app.route("/blog/<id>")
def get_blog(id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    post = response.json()[int(id)-1]
    print(post)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
