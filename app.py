from flask import Flask, render_template, redirect, url_for, request
from 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/user')
def user():
    return render_template('user.html')

if __name__ == "__main__":
    app.run(debug=True)
