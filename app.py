#importing for form functionality
from flask import Flask, render_template, url_for, redirect
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
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email')])
    password = PasswordField('Password', validators=[InputRequired(), length(min=8, max=12)])
    terms = BooleanField('Agree to Terms and Condtions', validators=[InputRequired()])

class User(object):  
    def __init__(self):
        self.username = ""
        self.password = ""

    def login(self, username, password):
        self.username = username
        self.password = password

    def signup(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

""""
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

"""

@app.route('/index')
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

#-----------------list functionality----------------#

shopping_dict = {}

@app.route('/user', methods=['GET', 'POST'])
def user():
    shopping = ShoppingList()
    shopping.name(shoppinglistname)
    shopping.additem(itemname)
    shopping.removeitem(itemname)
    shopping.addlist(shoppinglistname,items)
    shopping.removelist(shoppinglistname)
    
    return render_template("user.html")

if __name__ == "__main__":
    app.run(debug=True)
