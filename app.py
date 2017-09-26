#importing for form functionality
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, length


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'secretkey'
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), length(min=4, max=5)])
    password = PasswordField('Password', validators=[InputRequired(), length(min=8, max=12)])

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), length(min=4, max=5)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email')])
    password = PasswordField('Password', validators=[InputRequired(), length(min=8, max=12)])
    terms = BooleanField('Agree to Terms and Condtions', validators=[InputRequired()])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()

    if form.validate_on_submit():
        return redirect(url_for('login'))

    return render_template("sign_up.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect(url_for('user'))

    return render_template("login.html", form=form)

@app.route('/user')
def user():
    return render_template('user.html')

if __name__ == "__main__":
    app.run(debug=True)
