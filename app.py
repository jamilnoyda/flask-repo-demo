from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "you-will-never-guess"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
from flask import render_template, flash, redirect, url_for

SQLITE                  = 'sqlite'

# Table Names
USERS           = 'users'
ADDRESSES       = 'addresses'
from routes import *

from flask import render_template
from flask import request, render_template, jsonify
from forms import *
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
db.init_app(app)
from models import *

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()
    print("request",request)
    # if form.validate_on_submit():
        
    #     return redirect(url_for('index'))
    user  = AccountsUser()
    db.session.add(user)
    db.session.commit()

    return render_template(
        'login.html',
        title='Sign In',
        form=form
    )

@app.route('/')
def hello_world():
    return render_template(
        'index.html',
        title='Sign In',
        # form=form
    )



    

