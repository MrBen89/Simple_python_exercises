from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)

    Bootstrap(app)

    return app

app = create_app()

app.secret_key = "bob"

class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(min=8)])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Log In')



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    print(form.errors)
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
