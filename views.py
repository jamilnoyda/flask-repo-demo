@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)