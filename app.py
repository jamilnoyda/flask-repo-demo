from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "you-will-never-guess"
from flask import render_template, flash, redirect, url_for


from routes import *

from flask import render_template
from flask import request, render_template, jsonify
from forms import *
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()
    
    if form.validate_on_submit():
        
        return redirect(url_for('index'))

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



    

