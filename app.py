#importing for form functionality
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, length

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'secretkey'

#Form for login and sign-up
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), length(min=4, max=5)])
    password = PasswordField('Password', validators=[InputRequired(), length(min=8, max=12)])

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), length(min=4, max=5)])
    email = StringField('Email', validators=[InputRequired(), Email('Invalid email')])
    password = PasswordField('Password', validators=[InputRequired(), length(min=8, max=12)])
    terms = BooleanField('Agree to Terms and Condtions', validators=[InputRequired()])

#Object for user data handling
class User(object):
    userdict = {}
    
    def __init__(self):
        self.userlist = list()
        self.useraccount = list()

    def signup(self, username, email, password):
        self.useraccount = [username, email, password]
        self.logindetails = [email, password]
        self.userdict[username] = self.logindetails
        self.userlist.append(self.userdict)
        return self.userlist

class ShoppingList(object):    
    shopping_dict = {}

    #Creating a list for shopping lists and list for items on a shopping list
    def __init__(self):
        self.items = list()
        self.lists = list()

    #Method to name a list
    def name(self, listname):
        self.listname = listname
        
    #Method to add item
    def additem(self, item):
        self.items.append(item)
        return self.items

    #Method to remove item
    def removeitem(self, item):
        self.items.remove(item)
        return self.items

    #Method to link listname to items in dictionary  
    def addlist(self, listname, items):
        self.shopping_dict[listname] = items
        self.lists.append(self.shopping_dict)
        return self.lists

    #Method to remove list in dicionary
    def removelist(self, listname):
        for d in self.lists:
            if d.get(self.listname) == self.items:
                d.pop(self.listname)
        return self.lists


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()

    if form.validate_on_submit():
        user = User()

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user.signup(username, email, password)

        print(user.userlist)

        return redirect(url_for('login'))

    return render_template("sign_up.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User()
        username = request.form['username']
        password = request.form['password']

        if user.userdict[username] != username:
            error
            flash('user does not exit')
        else:
            return redirect(url_for('user'))

    else:
        return render_template("login.html", form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)