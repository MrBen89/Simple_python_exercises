from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY="API"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///films-collection.db'
db = SQLAlchemy(app)

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(400), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(400), nullable=True)
    img_url = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Film `self.title`>'

class EditForm(FlaskForm):
    rating = IntegerField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Update')

class AddForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Search')



@app.route("/")
def home():
    all_films = db.session.query(Film).all()
    return render_template("index.html", films=all_films)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    film_id = request.args.get("id")
    print(film_id)
    film = Film.query.get(film_id)
    if form.validate_on_submit():

        film.rating = float(form.rating.data)
        film.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html",form=form)

@app.route("/delete")
def delete():
    # DELETE A RECORD BY ID
    film_id = request.args.get("id")
    film = Film.query.get(film_id)
    db.session.delete(film)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        query = form.title.data
        response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&query={query}&page=1&include_adult=false")
        film_selections = response.json()["results"]
        return render_template("select.html",films=film_selections)
    return render_template("add.html",form=form)

@app.route("/find")
def find_film():
    film_api_id = request.args.get("id")
    if film_api_id:
        film_api_url = f"https://api.themoviedb.org/3/movie/{film_api_id}"
        #The language parameter is optional, if you were making the website for a different audience
        #e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(film_api_url, params={"api_key": API_KEY, "language": "en-US"})
        data = response.json()
        new_film = Film(
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            rating=0,
            review="Write a review",
            ranking=1,
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_film)
        db.session.commit()
        return redirect(url_for("home"))



#new_film = Film( title="Phone Booth",
#    year=2002,
#    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#    rating=7.3,
#    ranking=10,
#    review="My favourite character was the caller.",
#    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#)
#db.session.add(new_film)
#db.session.commit()

db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
