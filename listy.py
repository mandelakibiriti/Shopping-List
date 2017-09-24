from flask import Flask, render_template
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
def login():
    return render_template("user.html")
